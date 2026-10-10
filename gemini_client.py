import os
import sys
import re
import json
import base64
import time
import socket
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import (
    VISUAL_KEYS_FILE,
    VISUAL_GEMINI_MODEL,
    VISUAL_FALLBACK_MODELS,
    CHANNEL_NAME
)

socket.setdefaulttimeout(45)

def _load_keys(filepath: Path) -> List[str]:
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            keys = [k.strip() for k in f if k.strip() and not k.startswith("#")]
        if keys:
            return keys
    raise ValueError(f"Fichier de clés introuvable ou vide : {filepath}")

_VISUAL_KEYS = _load_keys(VISUAL_KEYS_FILE)
_VISUAL_IDX = [0]

STATS = {"visual_calls": 0, "rotations": 0, "failures": 0}

def call_gemini_visual(parts: List[Dict[str, Any]], retries: int = 4) -> str:
    """Appel pour l'analyse visuelle multimodale avec gemini-3.5-flash-lite et repli résilient."""
    models_to_try = [VISUAL_GEMINI_MODEL] + VISUAL_FALLBACK_MODELS
    
    for model in models_to_try:
        for attempt in range(retries):
            key = _VISUAL_KEYS[_VISUAL_IDX[0] % len(_VISUAL_KEYS)]
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
            payload = json.dumps({"contents": [{"parts": parts}]}).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
            
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    cands = data.get("candidates", [])
                    if cands and "content" in cands[0] and "parts" in cands[0]["content"]:
                        STATS["visual_calls"] += 1
                        return cands[0]["content"]["parts"][0].get("text", "")
            except urllib.error.HTTPError as e:
                _VISUAL_IDX[0] += 1
                STATS["rotations"] += 1
                if e.code in (429, 503, 500):
                    time.sleep(1.0)
                    continue
                err_text = e.read().decode("utf-8", "ignore")[:150]
                print(f"[Gemini-Visual] HTTPError {e.code} sur {model}: {err_text}", flush=True)
            except Exception as e:
                _VISUAL_IDX[0] += 1
                time.sleep(1.0)
                
    STATS["failures"] += 1
    return ""

def process_multimodal_block(
    candidate_frames: List[Dict[str, Any]],
    timestamp_str: str,
    verbatim_fr: str
) -> Dict[str, Any]:
    default_res = {
        "valid_frame_indices": [],
        "frame_captions": {},
        "interface": "Présentation orale ou séquence sans interface partagée.",
        "contenu": "Explications et conseils de création de contenu / IA.",
        "action": "Démonstration et mise en contexte pratique."
    }

    n_imgs = len(candidate_frames)
    if n_imgs == 0:
        return default_res

    img_list_txt = "\n".join([f"- Image #{i+1} : horodatage @ {cf.get('timestamp_str', '')}" for i, cf in enumerate(candidate_frames)])
    visual_prompt = (
        f"Tu es un analyste visuel pour la chaîne YouTube '{CHANNEL_NAME}' (segment {timestamp_str}).\n"
        f"Contexte audio du segment (en français) : {verbatim_fr[:350]}\n\n"
        f"Tu as reçu {n_imgs} capture(s) d'écran candidate(s) représentant des changements visuels :\n{img_list_txt}\n\n"
        "DIRECTIVE DE SÉLECTION D'IMAGES :\n"
        "- Retiens impérativement les images de démonstrations réelles : logiciels, sites web, interfaces d'outils IA, générateurs vidéo/image, dashboards, timeline de montage, fenêtres de réglages, prompts, captures d'écrans techniques.\n"
        "- Élimine les images purement floues ou les gros plans du youtubeur parlant face caméra sans aucun élément d'interface pertinent.\n\n"
        "Format STRICT obligatoire de ta réponse :\n"
        "[VALID_IMAGES] <numéros séparés par virgule (ex: 1, 2) ou AUCUNE>\n"
    )
    for i in range(n_imgs):
        visual_prompt += f"[DESC_IMAGE_{i+1}] <légende concise et informative en français décrivant l'écran affiché>\n"
    visual_prompt += (
        "[INTERFACE] <logiciels, sites ou environnements montrés à l'écran>\n"
        "[CONTENU] <textes, prompts, réglages, menus ou visuels observés>\n"
        "[ACTION] <action, test ou tutoriel effectué par le créateur>"
    )

    visual_parts: List[Dict[str, Any]] = [{"text": visual_prompt}]
    for cf in candidate_frames:
        img_path = cf.get("path")
        if img_path and isinstance(img_path, Path) and img_path.exists() and img_path.stat().st_size > 0:
            try:
                with open(img_path, "rb") as f:
                    b64_img = base64.b64encode(f.read()).decode("utf-8")
                visual_parts.append({
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": b64_img
                    }
                })
            except Exception:
                pass

    raw_vis = call_gemini_visual(visual_parts)
    if not raw_vis:
        return default_res

    res = dict(default_res)
    try:
        valid_indices = []
        frame_captions = {}
        if "[VALID_IMAGES]" in raw_vis:
            raw_val = raw_vis.split("[VALID_IMAGES]")[1]
            for m in ["[DESC_IMAGE_", "[INTERFACE]", "[CONTENU]", "[ACTION]"]:
                if m in raw_val:
                    raw_val = raw_val.split(m)[0]
            raw_val = raw_val.strip().upper()

            if "AUCUNE" not in raw_val and "NONE" not in raw_val and "ZERO" not in raw_val:
                if "TOUTES" in raw_val or "TOUT" in raw_val or "ALL" in raw_val:
                    valid_indices = list(range(n_imgs))
                else:
                    for token in re.findall(r'\b\d+\b', raw_val):
                        num = int(token)
                        if 1 <= num <= n_imgs:
                            valid_indices.append(num - 1)

        for i in range(n_imgs):
            tag = f"[DESC_IMAGE_{i+1}]"
            if tag in raw_vis:
                part_desc = raw_vis.split(tag)[1]
                for next_tag in [f"[DESC_IMAGE_{j+1}]" for j in range(i+1, n_imgs)] + ["[INTERFACE]", "[CONTENU]", "[ACTION]"]:
                    if next_tag in part_desc:
                        part_desc = part_desc.split(next_tag)[0]
                desc_text = part_desc.strip().lstrip(": -").strip()
                if desc_text and not desc_text.startswith("<"):
                    frame_captions[i] = desc_text

        res["valid_frame_indices"] = sorted(list(set(valid_indices)))
        res["frame_captions"] = frame_captions

        if "[INTERFACE]" in raw_vis:
            p_i = raw_vis.split("[INTERFACE]")[1]
            for m in ["[CONTENU]", "[ACTION]"]:
                if m in p_i:
                    p_i = p_i.split(m)[0]
            res["interface"] = p_i.strip()

        if "[CONTENU]" in raw_vis:
            p_c = raw_vis.split("[CONTENU]")[1]
            if "[ACTION]" in p_c:
                p_c = p_c.split("[ACTION]")[0]
            res["contenu"] = p_c.strip()

        if "[ACTION]" in raw_vis:
            res["action"] = raw_vis.split("[ACTION]")[1].strip()

    except Exception as e:
        print(f"[Gemini-Visual] Erreur parsing bloc visuel : {e}", flush=True)

    return res

def generate_executive_summary(video_title: str, full_verbatim_fr: str, tools_detected: List[str]) -> str:
    """Génère la Synthèse Exécutive (Résumé dense en 3 paragraphes, Outils, Points Clés)."""
    tools_str = ", ".join(tools_detected) if tools_detected else "Intelligence Artificielle, Vidéos IA, Outils No-Code & Agents, Montage Vidéo"
    prompt = (
        f"Tu es un rédacteur tech et analyste de contenu expert pour la chaîne YouTube '{CHANNEL_NAME}'.\n"
        f"Vidéo analysée : « {video_title} ».\n"
        f"Sujets et outils observés : {tools_str}\n\n"
        f"Transcription intégrale mot pour mot de la vidéo en français :\n\"\"\"\n{full_verbatim_fr[:12000]}\n\"\"\"\n\n"
        "RÉDIGE UNE SYNTHÈSE EXÉCUTIVE D'EXCELLENCE EN FRANÇAIS STRICTEMENT STRUCTURÉE COMME SUIT :\n\n"
        "### 💡 Résumé\n"
        "[Rédige exactement 3 paragraphes denses et fluides en gras/normal expliquant le sujet central, les nouveautés ou tutoriels présentés, la valeur pratique et les conclusions du créateur.]\n\n"
        "### 🛠️ Outils, Modèles & Logiciels Présentés\n"
        "[Liste à puces claire des logiciels, sites, modèles d'IA, outils de montage ou extensions montrés ou mentionnés]\n\n"
        "### 🔑 Points Clés & Enseignements Stratégiques\n"
        "[8 à 12 puces exhaustives résumant les conseils précis, astuces, configurations, avantages, cas d'usage et astuces de productivité livrés dans la vidéo.]\n\n"
        "Consigne : Ne mets pas d'introduction ni de conclusion méta, renvoie directement les 3 sections ci-dessus."
    )
    res = call_gemini_visual([{"text": prompt}])
    return res.strip() if res else ""
