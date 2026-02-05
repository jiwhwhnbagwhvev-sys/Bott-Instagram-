# ============================================================
#  CONFIGURATION MODULE
# ============================================================
#  Nama Project : Secure Terminal Login System
#  Deskripsi    : File konfigurasi utama untuk:
#                 - Login system
#                 - OTP verification
#                 - Telegram integration
#                 - Security & environment settings
#
#  PENTING !!!
#  - File ini WAJIB ada
#  - Semua module lain mengambil data dari sini
#  - Jangan ganti nama file
# ============================================================


# ============================================================
#  APPLICATION INFORMATION
# ============================================================

APP_NAME        = "Secure Terminal App"
APP_VERSION     = "1.0.0"
APP_AUTHOR      = "Private Developer"
APP_ENVIRONMENT = "PRODUCTION"   # DEVELOPMENT / PRODUCTION


# ============================================================
#  LOGIN SYSTEM CONFIGURATION
# ============================================================
#  Digunakan oleh login.py
#  User harus VALID untuk masuk ke menu utama
# ============================================================

# Username login utama
USERNAME = "admin"

# Password login utama
# NOTE:
# Saat ini masih plaintext
# Nanti bisa kita upgrade ke HASH (SHA256)
PASSWORD = "admin123"


# ============================================================
#  LOGIN SECURITY SETTINGS
# ============================================================

# Maksimal percobaan login
MAX_LOGIN_ATTEMPT = 3

# Delay (detik) setelah login gagal
LOGIN_FAIL_DELAY = 2


# ============================================================
#  TELEGRAM BOT CONFIGURATION
# ============================================================
#  Digunakan oleh otp_telegram.py
#  OTP akan dikirim ke Telegram
# ============================================================

# Token bot dari @BotFather
BOT_TOKEN = "ISI_BOT_TOKEN_KAMU"

# Chat ID Telegram (akun penerima OTP)
CHAT_ID = "ISI_CHAT_ID_KAMU"


# ============================================================
#  OTP SYSTEM CONFIGURATION
# ============================================================
#  Digunakan untuk sistem verifikasi OTP
# ============================================================

# Panjang OTP (6 digit)
OTP_LENGTH = 6

# Waktu berlaku OTP (detik)
OTP_EXPIRE_TIME = 60

# Maksimal percobaan input OTP
OTP_MAX_TRY = 3


# ============================================================
#  TERMINAL UI CONFIGURATION
# ============================================================
#  Warna dan tampilan terminal
# ============================================================

# ANSI COLOR CODES
COLOR_RESET  = "\033[0m"
COLOR_RED    = "\033[91m"
COLOR_GREEN  = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE   = "\033[94m"
COLOR_PURPLE = "\033[95m"
COLOR_CYAN   = "\033[96m"

# Logo settings
SHOW_LOGO = True
LOGO_STYLE = "LOCK_INSTAGRAM"


# ============================================================
#  LOGGING CONFIGURATION
# ============================================================
#  Untuk pengembangan lanjutan
# ============================================================

ENABLE_LOGGING = True
LOG_FILE_NAME = "system.log"

LOG_LOGIN_SUCCESS = True
LOG_LOGIN_FAILED  = True
LOG_OTP_ACTIVITY  = True


# ============================================================
#  SYSTEM FLAGS (INTERNAL USE)
# ============================================================

DEBUG_MODE = False
STRICT_VALIDATION = True


# ============================================================
#  END OF CONFIG FILE
# ============================================================
#  Jangan menulis kode program di file ini
#  File ini khusus konfigurasi
# ============================================================
