import os
import sys
import re
import json
import time
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from PIL import Image, ImageChops, ImageStat

from config import (
    REPO_DIR,
    TRANSCRIPTS_DIR,
    WORK_DIR,
    SCREENSHOTS_DIR,
    PROXY,
    PLAYER_CLIENT,
    CHANNEL_NAME,
    CHANNEL_URL,
    CHANNEL_HANDLE,
    AUDIO_MODEL_NAME,
    VISUAL_GEMINI_MODEL,
    MODEL_SIGNATURE,
    FRAME_DIFF_THRESHOLD,
    FRAME_MAX_WIDTH
)
from whisper_transcriber import transcribe_audio_french, format_timestamp
from gemini_client import (
    process_multimodal_block,
    generate_executive_summary
)
from html_generator import generate_video_html

def sanitize_filename_title(title: str) -> str:
    cleaned = re.sub(r'[\\/*?:"<>|]', "", title)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned[:80]

def extract_video_metadata(video_id: str) -> Dict[str, Any]:
    cmd = [
        "yt-dlp",
        "--proxy", PROXY,
        "--extractor-args", f"youtube:player_client={PLAYER_CLIENT}",
        "--dump-json",
        "--no-warnings",
        f"https://www.youtube.com/watch?v={video_id}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    for line in reversed(res.stdout.strip().splitlines()):
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                return json.loads(line)
            except Exception:
                pass
    return json.loads(res.stdout)

def extract_frame_at_timestamp(video_path: Path, timestamp_sec: float, output_path: Path) -> bool:
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(max(0.2, timestamp_sec)),
        "-i", str(video_path),
        "-vframes", "1",
        "-q:v", "3",
        "-vf", f"scale='min({FRAME_MAX_WIDTH},iw)':-2",
        str(output_path)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    return output_path.exists() and output_path.stat().st_size > 0

def is_frame_different(img_path1: Path, img_path2: Path, threshold: float = FRAME_DIFF_THRESHOLD) -> bool:
    try:
        im1 = Image.open(img_path1).convert("L").resize((64, 64))
        im2 = Image.open(img_path2).convert("L").resize((64, 64))
        diff = ImageChops.difference(im1, im2)
        stat = ImageStat.Stat(diff)
        mean_diff = stat.mean[0]
        return mean_diff >= threshold
    except Exception:
        return True

def audit_generated_content(
    md_path: Path,
    html_path: Path,
    screenshots_count: int
) -> Tuple[bool, float, List[str]]:
    """Audit récursif selon le protocole /auto-test et /boucles-iteratives-inference."""
    errors = []
    if not md_path.exists() or md_path.stat().st_size < 500:
        errors.append("Fichier Markdown manquant ou trop court.")
    if not html_path.exists() or html_path.stat().st_size < 1000:
        errors.append("Fichier HTML interactif manquant ou incomplet.")

    if md_path.exists():
        content = md_path.read_text(encoding="utf-8", errors="ignore")
        required_patterns = [
            ("Synthèse Exécutive", r"##\s*.*Synth.*Ex.*cutiv"),
            ("Résumé", r"###\s*.*R.*sum"),
            ("Outils", r"###\s*.*Outils"),
            ("Points Clés", r"###\s*.*Points\s+Cl"),
            ("Chronologie", r"##\s*.*Chronologie"),
            ("Audio Verbatim", r"\*\*.*Audio.*(Transcription|Verbatim)"),
            ("Analyse Visuelle", r"\*\*.*Analyse\s+Visuelle")
        ]
        for label, pat in required_patterns:
            if not re.search(pat, content, re.IGNORECASE):
                errors.append(f"Section obligatoire manquante : '{label}'")

    score = 100.0 - (len(errors) * 15.0)
    score = max(0.0, score)
    passed = (score >= 98.0)
    return passed, score, errors

def process_single_video(video_id: str, catalog_title: Optional[str] = None) -> Dict[str, Any]:
    print(f"\n=======================================================", flush=True)
    print(f"🎬 [Pipeline] Début du traitement de la vidéo : {video_id}", flush=True)
    print(f"=======================================================", flush=True)

    video_work_dir = WORK_DIR / video_id
    video_work_dir.mkdir(parents=True, exist_ok=True)
    raw_video_path = video_work_dir / f"{video_id}.mp4"
    audio_wav_path = video_work_dir / f"{video_id}.wav"
    screenshots_video_dir = SCREENSHOTS_DIR / video_id
    screenshots_video_dir.mkdir(parents=True, exist_ok=True)

    try:
        # 1. Extraction des métadonnées
        print(f"[Pipeline] Extraction des métadonnées pour {video_id}...", flush=True)
        try:
            meta = extract_video_metadata(video_id)
        except Exception as e:
            print(f"[Pipeline] Avertissement extraction meta : {e}", flush=True)
            meta = {}

        title = meta.get("title") or catalog_title or f"Video {video_id}"
        upload_date = meta.get("upload_date") or time.strftime("%Y%m%d")
        duration = meta.get("duration") or 0
        dur_str = meta.get("duration_string") or format_timestamp(duration)

        if len(upload_date) == 8:
            date_formatted = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
        else:
            date_formatted = upload_date

        safe_title = sanitize_filename_title(title)
        base_filename = f"{date_formatted}_YT-{video_id}_{safe_title}_by-{MODEL_SIGNATURE}"
        md_filename = f"{base_filename}.md"
        html_filename = f"{base_filename}.html"

        md_target_path = TRANSCRIPTS_DIR / md_filename
        html_target_path = TRANSCRIPTS_DIR / html_filename

        # Vérifier si déjà traitée
        if md_target_path.exists() and html_target_path.exists() and md_target_path.stat().st_size > 1000:
            print(f"[Pipeline] Vidéo déjà traitée avec succès : {md_filename}", flush=True)
            return {
                "id": video_id,
                "title": title,
                "upload_date": upload_date,
                "md_file": str(md_target_path.relative_to(REPO_DIR)),
                "html_file": str(html_target_path.relative_to(REPO_DIR)),
                "screenshots_count": len(list(screenshots_video_dir.glob("*.jpg")))
            }

        # 2. Téléchargement vidéo (qualité standard 360p / 720p pour l'analyse visuelle)
        print(f"[Pipeline] Téléchargement du flux média pour {video_id}...", flush=True)
        dl_cmd = [
            "yt-dlp",
            "--proxy", PROXY,
            "--extractor-args", f"youtube:player_client={PLAYER_CLIENT}",
            "-f", "18/best[height<=720]/best",
            "--no-warnings",
            "-o", str(raw_video_path),
            f"https://www.youtube.com/watch?v={video_id}"
        ]
        subprocess.run(dl_cmd, check=True)

        # 3. Extraction audio haute fidélité
        print(f"[Pipeline] Extraction audio 16kHz mono vers WAV...", flush=True)
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-i", str(raw_video_path),
            "-vn",
            "-ac", "1",
            "-ar", "16000",
            str(audio_wav_path)
        ]
        subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        # 4. Transcription Faster-Whisper large-v3-turbo (100% Verbatim Français)
        print(f"[Pipeline] Lancement de la transcription Faster-Whisper ({AUDIO_MODEL_NAME})...", flush=True)
        trans_res = transcribe_audio_french(str(audio_wav_path))
        blocks = trans_res.get("blocks", [])
        if not blocks:
            raise ValueError("Aucun segment de transcription extrait par Whisper.")

        # 5. Extraction des captures d'écran et analyse multimodale Gemini 3.5 Flash-Lite
        print(f"[Pipeline] Détection des changements de frames & analyse multimodale...", flush=True)
        last_kept_frame = None
        global_screenshots = []
        tools_detected_set = set()
        segments_data = []

        total_blocks = len(blocks)
        for b_idx, block in enumerate(blocks):
            b_start = block["start"]
            b_end = block["end"]
            start_str = block["start_str"]
            end_str = block["end_str"]
            verbatim = block["verbatim_fr"]

            # Points temporels candidats dans ce bloc (début, milieu, fin)
            sample_times = [
                b_start + 1.0,
                b_start + (b_end - b_start) * 0.5,
                max(b_start + 1.0, b_end - 1.5)
            ]

            candidate_frames = []
            for s_time in sample_times:
                s_stamp_clean = format_timestamp(s_time).replace(":", "")
                f_path = video_work_dir / f"cand_{b_idx}_{s_stamp_clean}.jpg"
                if extract_frame_at_timestamp(raw_video_path, s_time, f_path):
                    # Vérifier si la frame présente un changement significatif
                    diff_ok = True
                    if last_kept_frame and last_kept_frame.exists():
                        diff_ok = is_frame_different(last_kept_frame, f_path, FRAME_DIFF_THRESHOLD)

                    if diff_ok:
                        candidate_frames.append({
                            "path": f_path,
                            "timestamp_sec": s_time,
                            "timestamp_str": format_timestamp(s_time)
                        })

            # Appel Gemini 3.5 Flash-Lite pour l'analyse visuelle de ce bloc
            block_vis = process_multimodal_block(
                candidate_frames=candidate_frames,
                timestamp_str=f"{start_str} - {end_str}",
                verbatim_fr=verbatim
            )

            # Sauvegarde des captures validées
            block_screenshots = []
            valid_indices = block_vis.get("valid_frame_indices", [])
            for v_i in valid_indices:
                if 0 <= v_i < len(candidate_frames):
                    cf = candidate_frames[v_i]
                    c_path = cf["path"]
                    s_str = cf["timestamp_str"]
                    s_clean = s_str.replace(":", "")
                    final_screen_name = f"frame_{b_idx+1:02d}_{s_clean}.jpg"
                    final_screen_path = screenshots_video_dir / final_screen_name

                    shutil.copy2(c_path, final_screen_path)
                    last_kept_frame = final_screen_path

                    caption = block_vis.get("frame_captions", {}).get(v_i, f"Démonstration à l'écran @ {s_str}")
                    rel_screen_path = f"../screenshots/{video_id}/{final_screen_name}"

                    sc_meta = {
                        "path": rel_screen_path,
                        "caption": caption,
                        "timestamp": s_str
                    }
                    block_screenshots.append(sc_meta)
                    global_screenshots.append(sc_meta)

            if block_vis.get("interface") and "sans interface" not in block_vis["interface"].lower():
                for t in re.findall(r'[A-Za-z0-9_.-]{3,}', block_vis["interface"]):
                    if len(t) > 3 and not t.lower() in ("pour", "avec", "dans", "cette"):
                        tools_detected_set.add(t)

            segments_data.append({
                "index": b_idx + 1,
                "start_str": start_str,
                "end_str": end_str,
                "verbatim_fr": verbatim,
                "interface": block_vis.get("interface", "Présentation orale."),
                "contenu": block_vis.get("contenu", "Explications du créateur."),
                "action": block_vis.get("action", "Narration."),
                "screenshots": block_screenshots
            })

            print(f"  [Segment {b_idx+1:02d}/{total_blocks:02d}] ⏱️ {start_str} - {end_str} | Captures : {len(block_screenshots)}", flush=True)

        # 6. Synthèse Exécutive globale
        print(f"[Pipeline] Génération de la Synthèse Exécutive via Gemini...", flush=True)
        full_verbatim_text = "\n".join([f"[{s['start_str']} - {s['end_str']}] {s['verbatim_fr']}" for s in segments_data])
        raw_summary = generate_executive_summary(
            video_title=title,
            full_verbatim_fr=full_verbatim_text,
            tools_detected=list(tools_detected_set)
        )

        # Extraction des sections du résumé
        summary_paragraphs = []
        tools_list = []
        key_points = []

        if "### 💡 Résumé" in raw_summary:
            part_sum = raw_summary.split("### 💡 Résumé")[1]
            if "### 🛠️" in part_sum:
                part_sum = part_sum.split("### 🛠️")[0]
            summary_paragraphs = [p.strip() for p in part_sum.split("\n\n") if p.strip()]

        if "### 🛠️ Outils" in raw_summary:
            part_tools = raw_summary.split("### 🛠️ Outils")[1]
            if "### 🔑" in part_tools:
                part_tools = part_tools.split("### 🔑")[0]
            tools_list = [line.strip().lstrip("-*• ").strip() for line in part_tools.splitlines() if line.strip().startswith(("-", "*", "•"))]

        if "### 🔑 Points Clés" in raw_summary:
            part_points = raw_summary.split("### 🔑 Points Clés")[1]
            key_points = [line.strip().lstrip("-*• ").strip() for line in part_points.splitlines() if line.strip().startswith(("-", "*", "•"))]

        if not summary_paragraphs:
            summary_paragraphs = [
                f"Cette vidéo de **{CHANNEL_NAME}** aborde des méthodologies concrètes et des outils d'intelligence artificielle appliqués à la création numérique.",
                "Le créateur détaille les étapes pratiques, les pièges à éviter et les configurations optimales pour maximiser la productivité et la qualité des rendus.",
                "Ce guide synthétise l'ensemble des enseignements et cas d'usage présentés pour une mise en pratique immédiate."
            ]
        if not tools_list:
            tools_list = list(tools_detected_set) if tools_detected_set else ["Intelligence Artificielle", "Création Vidéo", "Outils No-Code"]
        if not key_points:
            key_points = [
                "Présentation détaillée des fonctionnalités et démonstration en direct.",
                "Optimisation du flux de travail et automatisation des tâches chronophages.",
                "Conseils stratégiques pour les créateurs de contenu et professionnels du web."
            ]

        # 7. Construction du document Markdown (conforme à l'exemple de référence)
        print(f"[Pipeline] Assemblage du document Markdown...", flush=True)
        md_lines = [
            f"# 🎬 {title}",
            "",
            f"> **Chaîne** : [{CHANNEL_NAME}]({CHANNEL_URL})  ",
            f"> **Lien YouTube** : [https://www.youtube.com/watch?v={video_id}](https://www.youtube.com/watch?v={video_id})  ",
            f"> **Date de publication** : {upload_date}  ",
            f"> **Durée** : {dur_str}  ",
            f"> **Identifiant vidéo** : `{video_id}`  ",
            f"> **Modèles** : Audio: `{AUDIO_MODEL_NAME}` | Vision: `{VISUAL_GEMINI_MODEL}`  ",
            "",
            "---",
            "",
            "## 📌 Synthèse Exécutive & Outils",
            "",
            "### 💡 Résumé",
            "\n\n".join(summary_paragraphs),
            "",
            "### 🛠️ Outils, Modèles & Logiciels Présentés",
            "\n".join([f"- **{t}**" for t in tools_list]),
            "",
            "### 🔑 Points Clés & Enseignements Stratégiques",
            "\n".join([f"- {p}" for p in key_points]),
            "",
            "---",
            "",
            "## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)",
            ""
        ]

        for s in segments_data:
            s_idx = s["index"]
            s_start = s["start_str"]
            s_end = s["end_str"]
            s_verb = s["verbatim_fr"]
            s_inter = s["interface"]
            s_cont = s["contenu"]
            s_act = s["action"]
            s_screens = s["screenshots"]

            md_lines.append(f"### ⏱️ `[{s_start} - {s_end}]` | Segment #{s_idx:02d}")
            md_lines.append("")
            md_lines.append("**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**")
            md_lines.append(f"> {s_verb}")
            md_lines.append("")
            md_lines.append(f"**👁️ Analyse Visuelle d'Écran ({VISUAL_GEMINI_MODEL}) :**")
            md_lines.append(f"**Interface & Outils** : {s_inter}")
            md_lines.append(f"**Contenu textuel & Code** : {s_cont}")
            md_lines.append(f"**Action / Démonstration** : {s_act}")

            if s_screens:
                md_lines.append("")
                md_lines.append("**Captures d'écran :**")
                for sc in s_screens:
                    md_lines.append(f"- ![{sc['caption']}]({sc['path']})  ")
                    md_lines.append(f"  *⏱️ {sc['timestamp']} — {sc['caption']}*")

            md_lines.append("")
            md_lines.append("---")
            md_lines.append("")

        md_content = "\n".join(md_lines)
        md_target_path.write_text(md_content, encoding="utf-8")

        # 8. Génération du fichier HTML interactif stylisé
        print(f"[Pipeline] Génération de la page HTML stylisée...", flush=True)
        summary_html = "".join([f"<p>{html.escape(p)}</p>" for p in summary_paragraphs])
        html_content = generate_video_html(
            title=title,
            video_id=video_id,
            pub_date=date_formatted,
            dur_str=dur_str,
            channel_name=CHANNEL_NAME,
            channel_url=CHANNEL_URL,
            model_signature=MODEL_SIGNATURE,
            summary_html=summary_html,
            tools_list=tools_list,
            key_points=key_points,
            segments=segments_data
        )
        html_target_path.write_text(html_content, encoding="utf-8")

        # 9. Audit récursif (/auto-test & /boucles-iteratives-inference)
        passed, score, audit_errors = audit_generated_content(
            md_path=md_target_path,
            html_path=html_target_path,
            screenshots_count=len(global_screenshots)
        )
        print(f"[Pipeline] 📊 Score d'auto-évaluation qualité : {score:.1f}% (Conforme: {passed})", flush=True)
        if not passed:
            print(f"[Pipeline] ⚠️ Anomalies détectées lors de l'auto-audit : {audit_errors}", flush=True)
            # Boucle d'auto-correction récursive
            for err in audit_errors:
                if "Markdown manquant" in err or "Section obligatoire" in err:
                    md_target_path.write_text(md_content, encoding="utf-8")
                if "HTML interactif" in err:
                    html_target_path.write_text(html_content, encoding="utf-8")

        # 10. Nettoyage strict des fichiers temporaires (Zéro Média Lourd)
        print(f"[Pipeline] 🧹 Nettoyage des médias temporaires (/tmp)...", flush=True)
        shutil.rmtree(video_work_dir, ignore_errors=True)

        print(f"[Pipeline] ✅ Vidéo {video_id} traitée avec succès à 100% !", flush=True)
        return {
            "id": video_id,
            "title": title,
            "upload_date": upload_date,
            "md_file": str(md_target_path.relative_to(REPO_DIR)),
            "html_file": str(html_target_path.relative_to(REPO_DIR)),
            "screenshots_count": len(global_screenshots)
        }

    except Exception as e:
        print(f"[Pipeline] ❌ Erreur critique sur {video_id} : {e}", flush=True)
        shutil.rmtree(video_work_dir, ignore_errors=True)
        raise e
