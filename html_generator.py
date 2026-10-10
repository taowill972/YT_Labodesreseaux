import html
from pathlib import Path
from typing import List, Dict, Any

def generate_video_html(
    title: str,
    video_id: str,
    pub_date: str,
    dur_str: str,
    channel_name: str,
    channel_url: str,
    model_signature: str,
    summary_html: str,
    tools_list: List[str],
    key_points: List[str],
    segments: List[Dict[str, Any]]
) -> str:
    """
    Génère une page HTML moderne, responsive et élégante.
    Supporte de multiples captures d'écran par bloc temporel en grille adaptative,
    avec filtrage des plans face-caméra et mise en valeur des démonstrations d'écrans.
    """

    tools_badges = "".join([f'<span class="tool-tag">{html.escape(t)}</span>' for t in tools_list])
    points_items = "".join([f'<li><span class="point-bullet">✦</span><span>{html.escape(p)}</span></li>' for p in key_points])

    timeline_items = []
    for s in segments:
        idx = s.get("index", 1)
        start_str = s.get("start_str", "00:00:00")
        end_str = s.get("end_str", "00:00:00")
        verbatim = html.escape(s.get("verbatim_fr", ""))
        interface = html.escape(s.get("interface", ""))
        contenu = html.escape(s.get("contenu", ""))
        action = html.escape(s.get("action", ""))

        screenshots_list = s.get("screenshots", [])
        if not screenshots_list and s.get("screenshot_rel"):
            screenshots_list = [{
                "path": s.get("screenshot_rel"),
                "caption": f"Démonstration à l'écran @ {start_str}",
                "timestamp": start_str
            }]

        img_html = ""
        if screenshots_list:
            cards = []
            for sc in screenshots_list:
                img_path = html.escape(sc.get("path", ""))
                cap = html.escape(sc.get("caption", f"Démonstration @ {sc.get('timestamp', start_str)}"))
                t_str = html.escape(sc.get("timestamp", start_str))
                cards.append(f'''
                <div class="screenshot-card">
                    <div class="img-wrapper">
                        <img src="{img_path}" alt="{cap}" loading="lazy" onclick="openLightbox('{img_path}')">
                        <span class="zoom-badge">🔍 Agrandir</span>
                    </div>
                    <div class="screenshot-caption">
                        <span class="caption-time">⏱️ {t_str}</span>
                        <span class="caption-text">{cap}</span>
                    </div>
                </div>
                ''')

            count_class = f"count-{min(len(screenshots_list), 4)}"
            img_html = f'''
            <div class="segment-screenshots-wrapper">
                <div class="screenshots-header">
                    <span class="media-icon">📸</span>
                    <strong>Démonstration(s) à l'écran ({len(screenshots_list)}) :</strong>
                </div>
                <div class="segment-screenshots-grid {count_class}">
                    {"".join(cards)}
                </div>
            </div>
            '''

        card = f'''
        <div class="timeline-block" id="segment-{idx}">
            <div class="timeline-time">
                <span class="time-badge">⏱️ {start_str} - {end_str}</span>
                <span class="segment-idx">Segment #{idx:02d}</span>
            </div>
            <div class="timeline-content">
                <div class="verbatim-box">
                    <div class="verbatim-header">
                        <span class="speaker-icon">🔊</span>
                        <strong>Audio Verbatim (Mot pour Mot en Français) :</strong>
                    </div>
                    <blockquote class="verbatim-text">{verbatim}</blockquote>
                </div>
                <div class="visual-box">
                    <div class="visual-header">
                        <span class="eye-icon">👁️</span>
                        <strong>Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :</strong>
                    </div>
                    <div class="visual-details">
                        <p><strong>Interface & Outils :</strong> {interface}</p>
                        <p><strong>Contenu textuel & Code :</strong> {contenu}</p>
                        <p><strong>Action / Démonstration :</strong> {action}</p>
                    </div>
                </div>
                {img_html}
            </div>
        </div>
        '''
        timeline_items.append(card)

    timeline_html = "\n".join(timeline_items)

    html_code = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎬 {html.escape(title)} — Labo des Réseaux</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #090d16;
            --bg-surface: #0f172a;
            --bg-card: #141e33;
            --bg-card-hover: #1a2744;
            --border-color: #243452;
            --border-light: rgba(99, 102, 241, 0.2);
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.35);
            --secondary: #8b5cf6;
            --accent: #f43f5e;
            --success: #10b981;
            --text-title: #f8fafc;
            --text-main: #cbd5e1;
            --text-muted: #8292ab;
            --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: var(--font-main);
            line-height: 1.65;
            padding: 2rem 1rem;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1180px;
            margin: 0 auto;
        }}

        /* Header */
        header.video-header {{
            background: linear-gradient(135deg, rgba(20, 30, 51, 0.95), rgba(15, 23, 42, 0.98));
            border: 1px solid var(--border-color);
            border-radius: 1.25rem;
            padding: 2.2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5), 0 0 20px -5px var(--primary-glow);
            backdrop-filter: blur(12px);
        }}

        h1.video-title {{
            font-size: 1.85rem;
            font-weight: 800;
            color: var(--text-title);
            line-height: 1.35;
            margin-bottom: 1.2rem;
            letter-spacing: -0.02em;
        }}

        .meta-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
            align-items: center;
        }}

        .badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.35rem 0.85rem;
            border-radius: 9999px;
            font-size: 0.82rem;
            font-weight: 500;
            background: rgba(36, 52, 82, 0.6);
            color: var(--text-main);
            border: 1px solid var(--border-color);
        }}

        .badge-primary {{
            background: rgba(99, 102, 241, 0.15);
            color: #a5b4fc;
            border-color: rgba(99, 102, 241, 0.4);
        }}

        .badge-yt {{
            background: rgba(244, 63, 94, 0.15);
            color: #fda4af;
            border-color: rgba(244, 63, 94, 0.4);
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .badge-yt:hover {{
            background: rgba(244, 63, 94, 0.3);
            transform: translateY(-1px);
        }}

        /* Executive Summary Section */
        section.executive-summary {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 1.25rem;
            padding: 2.2rem;
            margin-bottom: 2.5rem;
        }}

        .section-title {{
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--text-title);
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid var(--border-color);
        }}

        .summary-card {{
            background: var(--bg-card);
            border-radius: 0.85rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-left: 4px solid var(--primary);
        }}
        .summary-card p {{
            margin-bottom: 0.9rem;
            color: var(--text-main);
            font-size: 0.98rem;
        }}
        .summary-card p:last-child {{
            margin-bottom: 0;
        }}

        .tools-box {{
            margin-bottom: 1.5rem;
        }}
        .tools-box h3, .points-box h3 {{
            font-size: 1.05rem;
            color: #e2e8f0;
            margin-bottom: 0.85rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .tools-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .tool-tag {{
            background: rgba(30, 41, 59, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.2);
            color: #e2e8f0;
            padding: 0.35rem 0.8rem;
            border-radius: 0.5rem;
            font-size: 0.85rem;
            font-weight: 500;
        }}

        .points-box ul {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.65rem;
        }}

        .points-box li {{
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            background: var(--bg-card);
            padding: 0.85rem 1.1rem;
            border-radius: 0.65rem;
            font-size: 0.92rem;
            color: #cbd5e1;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }}

        .point-bullet {{
            color: var(--primary);
            font-size: 1rem;
            line-height: 1.4;
        }}

        /* Timeline Section */
        section.timeline-section {{
            margin-top: 2rem;
        }}

        .timeline-block {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 1rem;
            margin-bottom: 1.8rem;
            overflow: hidden;
            transition: border-color 0.2s ease;
        }}
        .timeline-block:hover {{
            border-color: rgba(99, 102, 241, 0.4);
        }}

        .timeline-time {{
            background: rgba(20, 30, 51, 0.7);
            padding: 0.85rem 1.4rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .time-badge {{
            font-family: var(--font-mono);
            font-size: 0.9rem;
            font-weight: 600;
            color: #93c5fd;
            background: rgba(59, 130, 246, 0.15);
            padding: 0.25rem 0.65rem;
            border-radius: 0.35rem;
            border: 1px solid rgba(59, 130, 246, 0.3);
        }}

        .segment-idx {{
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .timeline-content {{
            padding: 1.4rem;
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }}

        .verbatim-box {{
            background: rgba(15, 23, 42, 0.6);
            border-left: 3px solid #10b981;
            border-radius: 0.5rem;
            padding: 1rem 1.2rem;
        }}

        .verbatim-header, .visual-header, .screenshots-header {{
            font-size: 0.85rem;
            color: #94a3b8;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.45rem;
        }}

        .verbatim-text {{
            font-size: 0.96rem;
            line-height: 1.65;
            color: #f1f5f9;
            font-style: italic;
        }}

        .visual-box {{
            background: rgba(20, 30, 51, 0.5);
            border-left: 3px solid #8b5cf6;
            border-radius: 0.5rem;
            padding: 1rem 1.2rem;
        }}

        .visual-details p {{
            font-size: 0.91rem;
            margin-bottom: 0.45rem;
            color: #cbd5e1;
        }}
        .visual-details p:last-child {{
            margin-bottom: 0;
        }}

        .visual-details strong {{
            color: #e2e8f0;
        }}

        /* Screenshots grid */
        .segment-screenshots-wrapper {{
            background: rgba(10, 16, 28, 0.7);
            border-radius: 0.75rem;
            padding: 1rem;
            border: 1px dashed rgba(148, 163, 184, 0.2);
        }}

        .segment-screenshots-grid {{
            display: grid;
            gap: 1rem;
            margin-top: 0.65rem;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        }}

        .screenshot-card {{
            background: #0b1120;
            border-radius: 0.6rem;
            overflow: hidden;
            border: 1px solid var(--border-color);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .screenshot-card:hover {{
            transform: translateY(-2px);
            border-color: var(--primary);
        }}

        .img-wrapper {{
            position: relative;
            cursor: pointer;
            overflow: hidden;
            aspect-ratio: 16 / 9;
            background: #000;
        }}

        .img-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.3s ease;
        }}
        .img-wrapper:hover img {{
            transform: scale(1.03);
        }}

        .zoom-badge {{
            position: absolute;
            bottom: 0.5rem;
            right: 0.5rem;
            background: rgba(0, 0, 0, 0.75);
            color: #fff;
            padding: 0.2rem 0.55rem;
            border-radius: 0.35rem;
            font-size: 0.75rem;
            backdrop-filter: blur(4px);
            opacity: 0;
            transition: opacity 0.2s ease;
        }}
        .img-wrapper:hover .zoom-badge {{
            opacity: 1;
        }}

        .screenshot-caption {{
            padding: 0.65rem 0.85rem;
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
        }}

        .caption-time {{
            font-family: var(--font-mono);
            font-size: 0.75rem;
            color: #93c5fd;
        }}

        .caption-text {{
            font-size: 0.82rem;
            color: #94a3b8;
            line-height: 1.4;
        }}

        /* Lightbox modal */
        #lightbox {{
            display: none;
            position: fixed;
            z-index: 9999;
            inset: 0;
            background: rgba(0, 0, 0, 0.92);
            backdrop-filter: blur(8px);
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }}
        #lightbox.active {{
            display: flex;
        }}
        #lightbox img {{
            max-width: 95vw;
            max-height: 90vh;
            border-radius: 0.5rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        }}
        #lightbox-close {{
            position: absolute;
            top: 1.5rem;
            right: 2rem;
            color: #fff;
            font-size: 2.2rem;
            cursor: pointer;
            line-height: 1;
        }}

        footer {{
            text-align: center;
            margin-top: 3rem;
            padding: 1.5rem;
            color: var(--text-muted);
            font-size: 0.85rem;
            border-top: 1px solid var(--border-color);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="video-header">
            <h1 class="video-title">🎬 {html.escape(title)}</h1>
            <div class="meta-badges">
                <span class="badge badge-primary">📺 {html.escape(channel_name)}</span>
                <a href="https://www.youtube.com/watch?v={html.escape(video_id)}" target="_blank" rel="noopener" class="badge badge-yt">
                    ▶️ Voir sur YouTube ({html.escape(video_id)})
                </a>
                <span class="badge">📅 {html.escape(pub_date)}</span>
                <span class="badge">⏱️ {html.escape(dur_str)}</span>
                <span class="badge">🤖 {html.escape(model_signature)}</span>
            </div>
        </header>

        <section class="executive-summary">
            <h2 class="section-title">📌 Synthèse Exécutive & Outils</h2>
            
            <div class="summary-card">
                {summary_html}
            </div>

            <div class="tools-box">
                <h3>🛠️ Outils, Modèles & Logiciels Présentés</h3>
                <div class="tools-grid">
                    {tools_badges}
                </div>
            </div>

            <div class="points-box">
                <h3>🔑 Points Clés & Enseignements Stratégiques</h3>
                <ul>
                    {points_items}
                </ul>
            </div>
        </section>

        <section class="timeline-section">
            <h2 class="section-title">⏱️ Chronologie & Transcription Complète Audio & Visuelle</h2>
            {timeline_html}
        </section>

        <footer>
            Généré automatiquement par l'agent de veille multimodale Antigravity — Pipeline Whisper-v3-large-turbo & Gemini-3.5-flash-lite.
        </footer>
    </div>

    <div id="lightbox" onclick="closeLightbox()">
        <span id="lightbox-close">&times;</span>
        <img id="lightbox-img" src="" alt="Capture plein écran" onclick="event.stopPropagation()">
    </div>

    <script>
        function openLightbox(src) {{
            const lb = document.getElementById('lightbox');
            const img = document.getElementById('lightbox-img');
            img.src = src;
            lb.classList.add('active');
        }}
        function closeLightbox() {{
            document.getElementById('lightbox').classList.remove('active');
        }}
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeLightbox();
        }});
    </script>
</body>
</html>
'''
    return html_code
