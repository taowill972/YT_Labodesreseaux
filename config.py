from pathlib import Path
import os

# Detect environment: VPS /root or local
if Path("/root/YT_Labodesreseaux").exists() or os.name != "nt":
    BASE_DIR = Path("/root/YT_Labodesreseaux")
    WORK_DIR = Path("/tmp/yt_labodesreseaux_work")
else:
    BASE_DIR = Path(__file__).resolve().parent
    WORK_DIR = BASE_DIR / "tmp_work"

REPO_DIR = BASE_DIR
TRANSCRIPTS_DIR = BASE_DIR / "YT_Labodesreseaux_Transcript"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
CATALOG_FILE = BASE_DIR / "catalog.json"
STATE_FILE = BASE_DIR / "state.json"
LOG_FILE = Path("/var/log/yt_labodesreseaux.log") if os.name != "nt" else BASE_DIR / "yt_labodesreseaux.log"

# Channel Details
CHANNEL_ID = "UCMJEpQVv0p3qzJnQ9IuiiMA"
CHANNEL_NAME = "Labo Des Réseaux"
CHANNEL_HANDLE = "@labodesreseaux"
CHANNEL_URL = "https://www.youtube.com/@labodesreseaux"
RSS_FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
CHANNEL_DOMAIN = "Intelligence Artificielle, Vidéos IA, Outils No-Code & Agents, Montage Vidéo, Création de Contenu, Réseaux Sociaux, Tutos & Astuces Web"

# Models
WHISPER_MODEL = "large-v3-turbo"
AUDIO_MODEL_NAME = "whisper-v3-large-turbo"

VISUAL_GEMINI_MODEL = "gemini-3.5-flash-lite"
VISUAL_FALLBACK_MODELS = ["gemini-2.5-flash-lite"]

MODEL_SIGNATURE = f"{AUDIO_MODEL_NAME}+{VISUAL_GEMINI_MODEL}"

# API Keys & Network
VISUAL_KEYS_FILE = BASE_DIR / "gemini_visual_keys.txt"
PROXY = "socks5://127.0.0.1:4001"
PLAYER_CLIENT = "android"

# Processing parameters
BATCH_SIZE = 7
MAX_BLOCK_DURATION = 32.0
MIN_BLOCK_DURATION = 18.0
FRAME_DIFF_THRESHOLD = 14.0
FRAME_MAX_WIDTH = 1280

# Ensure directories exist
BASE_DIR.mkdir(parents=True, exist_ok=True)
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
WORK_DIR.mkdir(parents=True, exist_ok=True)
