import os
import sys
import time
import json
import signal
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import (
    BASE_DIR,
    CATALOG_FILE,
    STATE_FILE,
    CHANNEL_ID,
    CHANNEL_NAME,
    PROXY,
    PLAYER_CLIENT
)
from pipeline import process_single_video
from git_manager import update_readme_index, commit_and_push_repo

POLL_INTERVAL_SECONDS = 900  # 15 minutes entre chaque interrogation

running = True

def handle_signal(sig, frame):
    global running
    print(f"\n[Listener] Signal {sig} reçu, arrêt propre du démon d'écoute...", flush=True)
    running = False

signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

def load_state() -> Dict[str, Any]:
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"processed_ids": [], "processed_videos": [], "completed_count": 0}

def save_state(state: Dict[str, Any]) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def fetch_latest_channel_videos() -> List[Dict[str, str]]:
    """
    Interroge YouTube sans consommer AUCUN token LLM via yt-dlp flat-playlist + proxy socks5.
    """
    cmd = [
        "yt-dlp",
        "--proxy", PROXY,
        "--extractor-args", f"youtube:player_client={PLAYER_CLIENT}",
        "--flat-playlist",
        "--playlist-end", "5",
        "--dump-json",
        f"https://www.youtube.com/channel/{CHANNEL_ID}/videos"
    ]
    videos = []
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        for line in res.stdout.strip().splitlines():
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            videos.append({
                "id": data.get("id"),
                "title": data.get("title", ""),
                "published": data.get("upload_date", "")
            })
    except Exception as e:
        print(f"[Listener] Erreur extraction yt-dlp : {e}", flush=True)

    return videos

def main():
    print(f"\n=======================================================", flush=True)
    print(f"📡 [Listener] Démarrage de l'écoute Passive Zéro-Token", flush=True)
    print(f"📺 Chaîne : {CHANNEL_NAME} ({CHANNEL_ID})", flush=True)
    print(f"⏱️ Intervalle de vérification : {POLL_INTERVAL_SECONDS} secondes (15 min)", flush=True)
    print(f"💡 Solution : Extraction yt-dlp avec SOCKS5 proxy (0 token LLM consommé)", flush=True)
    print(f"=======================================================\n", flush=True)

    # Initialisation de la baseline des IDs connus
    known_ids = set()
    if CATALOG_FILE.exists():
        try:
            with open(CATALOG_FILE, "r", encoding="utf-8") as f:
                cat = json.load(f)
                for item in cat:
                    if item.get("id"):
                        known_ids.add(item["id"])
        except Exception:
            pass

    state = load_state()
    for pid in state.get("processed_ids", []):
        known_ids.add(pid)

    print(f"[Listener] Baseline initialisée avec {len(known_ids)} IDs connus.", flush=True)

    while running:
        t_now = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
        print(f"[{t_now}] [Listener] Vérification des nouvelles publications...", flush=True)

        latest_videos = fetch_latest_channel_videos()
        new_found = []

        for v in latest_videos:
            vid_id = v.get("id")
            if vid_id and vid_id not in known_ids:
                print(f"[Listener] 🔔 NOUVELLE VIDÉO DÉTECTÉE : {vid_id} — {v.get('title')}", flush=True)
                new_found.append(v)
                known_ids.add(vid_id)

        if new_found:
            # Traiter les nouvelles vidéos de la plus ancienne à la plus récente parmi les nouvelles
            for nv in reversed(new_found):
                vid_id = nv["id"]
                title = nv.get("title", "")
                print(f"\n[Listener] 🚀 Lancement immédiat du pipeline pour la nouvelle vidéo : {vid_id}", flush=True)
                try:
                    res = process_single_video(vid_id, catalog_title=title)

                    # Mise à jour du catalogue
                    if CATALOG_FILE.exists():
                        try:
                            with open(CATALOG_FILE, "r", encoding="utf-8") as f:
                                cat_data = json.load(f)
                            cat_data.insert(0, {
                                "id": vid_id,
                                "title": title,
                                "upload_date": res.get("upload_date", ""),
                                "webpage_url": f"https://www.youtube.com/watch?v={vid_id}"
                            })
                            with open(CATALOG_FILE, "w", encoding="utf-8") as f:
                                json.dump(cat_data, f, ensure_ascii=False, indent=2)
                        except Exception as e:
                            print(f"[Listener] Erreur mise à jour catalogue : {e}", flush=True)

                    # Mise à jour de l'état
                    state = load_state()
                    if vid_id not in state["processed_ids"]:
                        state["processed_ids"].append(vid_id)
                        state["processed_videos"].append(res)
                        state["completed_count"] = len(state["processed_ids"])
                        state["last_detected_new"] = vid_id
                        save_state(state)

                    update_readme_index(state["processed_videos"], total_catalog_count=len(known_ids))
                    commit_and_push_repo(f"feat(listener): nouvelle vidéo transcrite {vid_id} — {title[:50]}")
                    print(f"[Listener] ✅ Nouvelle vidéo {vid_id} intégrée et synchronisée avec succès !", flush=True)
                except Exception as e:
                    print(f"[Listener] ❌ Erreur lors du traitement de {vid_id} : {e}", flush=True)

        # Attente passive avant le prochain cycle
        for _ in range(POLL_INTERVAL_SECONDS):
            if not running:
                break
            time.sleep(1)

    print("[Listener] Arrêt propre du démon d'écoute passif terminé.", flush=True)

if __name__ == "__main__":
    main()
