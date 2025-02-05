import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(env_path)

# webhook url
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# chrome configuration
CHROME_OPTIONS = [
    '--headless',
    '--no-sandbox',
    '--disable-dev-shm-usage'
]

# sirama configuration
SIRAMA_LOGIN_URL = "https://sirama.telkomuniversity.ac.id/auth/login"
SIRAMA_BASE_URL = "https://sirama.telkomuniversity.ac.id"

# api configuration 
SIRAMA_API_BASE = os.getenv("SIRAMA_API_BASE")
MATKUL_TERSEDIA = os.getenv("MATKUL_TERSEDIA")
MATKUL_DIPILIH = os.getenv("MATKUL_DIPILIH")
ID_FAKULTAS = os.getenv("ID_FAKULTAS")

# credentials siramamu yang diambil dari env lee
USERNAME = os.getenv("SIRAMA_USERNAME")
PASSWORD = os.getenv("SIRAMA_PASSWORD")

# verif semua environment
required_vars = [
    "SIRAMA_USERNAME",
    "SIRAMA_PASSWORD",
    "SIRAMA_API_BASE",
    "MATKUL_TERSEDIA",
    "MATKUL_DIPILIH",
    "ID_FAKULTAS"
]

missing_vars = [var for var in required_vars if not os.getenv(var.upper())]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {
                     ', '.join(missing_vars)}")