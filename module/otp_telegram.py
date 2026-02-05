# ============================================================
#  OTP TELEGRAM MODULE
# ============================================================
#  File       : otp_telegram.py
#  Deskripsi  : Sistem OTP profesional menggunakan Telegram
#
#  Fitur :
#  - Generate OTP acak
#  - Kirim OTP real ke Telegram Bot
#  - Expired OTP
#  - Limit percobaan input OTP
#  - Validasi ketat
#
#  Digunakan oleh :
#  - main.py
#
#  Bergantung pada :
#  - config.py
# ============================================================

import random
import time
import requests
import sys
import config


# ============================================================
#  OTP UTILITY FUNCTIONS
# ============================================================

def generate_otp():
    """
    Generate OTP berdasarkan panjang yang ditentukan
    di config.py
    """
    start = 10 ** (config.OTP_LENGTH - 1)
    end   = (10 ** config.OTP_LENGTH) - 1
    return random.randint(start, end)


def current_timestamp():
    """
    Mengambil timestamp saat ini
    """
    return int(time.time())


def is_otp_expired(expire_time):
    """
    Mengecek apakah OTP sudah kadaluarsa
    """
    return current_timestamp() > expire_time


# ============================================================
#  TELEGRAM FUNCTIONS
# ============================================================

def send_telegram_message(message):
    """
    Mengirim pesan ke Telegram menggunakan Bot API
    """
    url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": config.CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(config.COLOR_RED + "❌ Gagal mengirim OTP ke Telegram")
        print("Error:", e)
        print(config.COLOR_RESET)
        return False


# ============================================================
#  OTP PROCESS
# ============================================================

def send_and_verify_otp(target_number):
    """
    Proses utama OTP:
    1. Generate OTP
    2. Kirim ke Telegram
    3. Validasi input user
    """

    otp_code = generate_otp()
    expire_time = current_timestamp() + config.OTP_EXPIRE_TIME
    attempt = 0

    message = (
        "🔐 <b>OTP VERIFICATION</b>\n"
        "============================\n"
        f"📱 Nomor : {target_number}\n"
        f"🔢 Kode  : <b>{otp_code}</b>\n"
        f"⏱ Berlaku : {config.OTP_EXPIRE_TIME} detik\n"
        "============================"
    )

    print(config.COLOR_YELLOW + "\nMengirim OTP ke Telegram...")
    print(config.COLOR_RESET)

    if not send_telegram_message(message):
        print(config.COLOR_RED + "❌ Proses OTP dibatalkan")
        print(config.COLOR_RESET)
        return False

    print(config.COLOR_GREEN + "📩 OTP berhasil dikirim")
    print(config.COLOR_RESET)

    # ========================================================
    #  OTP INPUT VALIDATION LOOP
    # ========================================================

    while attempt < config.OTP_MAX_TRY:
        user_input = input("Masukkan OTP : ").strip()

        if is_otp_expired(expire_time):
            print()
            print(config.COLOR_RED + "❌ OTP KADALUARSA")
            print("Silakan minta OTP baru")
            print(config.COLOR_RESET)
            return False

        if user_input == str(otp_code):
            print()
            print(config.COLOR_GREEN + "✅ OTP VALID")
            print("Verifikasi berhasil")
            print(config.COLOR_RESET)
            return True
        else:
            attempt += 1
            print()
            print(config.COLOR_RED + "❌ OTP SALAH")
            print(f"Sisa percobaan : {config.OTP_MAX_TRY - attempt}")
            print(config.COLOR_RESET)

    print()
    print(config.COLOR_RED + "⛔ OTP DIBLOKIR")
    print("Terlalu banyak percobaan gagal")
    print(config.COLOR_RESET)
    return False


# ============================================================
#  END OF FILE
# ============================================================
