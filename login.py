# ============================================================
#  LOGIN MODULE
# ============================================================
#  File       : login.py
#  Deskripsi  : Sistem login terminal dengan validasi ketat
#               dan tampilan logo berwarna
#
#  Digunakan oleh :
#  - main.py
#
#  Bergantung pada :
#  - config.py
# ============================================================

import os
import time
import sys

# Import konfigurasi
import config


# ============================================================
#  TERMINAL UTILITY FUNCTIONS
# ============================================================

def clear_screen():
    """
    Membersihkan layar terminal
    """
    os.system("clear")


def slow_print(text, delay=0.02):
    """
    Menampilkan teks dengan efek mengetik
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ============================================================
#  LOGO & UI FUNCTIONS
# ============================================================

def show_logo():
    """
    Menampilkan logo terminal
    Warna : Kuning & Hijau
    Icon  : Gembok + Instagram
    """
    print(config.COLOR_YELLOW)
    print(" ███████╗ ███████╗ ██████╗ ██╗   ██╗██████╗ ")
    print(" ██╔════╝ ██╔════╝██╔════╝ ██║   ██║██╔══██╗")
    print(" ███████╗ █████╗  ██║  ███╗██║   ██║██████╔╝")
    print(" ╚════██║ ██╔══╝  ██║   ██║██║   ██║██╔══██╗")
    print(" ███████║ ███████╗╚██████╔╝╚██████╔╝██║  ██║")
    print(" ╚══════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝")
    print()
    print(config.COLOR_GREEN + "        🔒  INSTAGRAM SECURE LOGIN")
    print(config.COLOR_GREEN + "================================================")
    print(config.COLOR_RESET)


def show_app_info():
    """
    Menampilkan informasi aplikasi
    """
    print(f"{config.COLOR_CYAN}App Name   : {config.APP_NAME}")
    print(f"Version    : {config.APP_VERSION}")
    print(f"Environment: {config.APP_ENVIRONMENT}")
    print(config.COLOR_RESET)
    print()


# ============================================================
#  LOGIN VALIDATION FUNCTIONS
# ============================================================

def validate_username(input_username):
    """
    Validasi username
    """
    if not input_username:
        return False
    if config.STRICT_VALIDATION:
        return input_username == config.USERNAME
    return True


def validate_password(input_password):
    """
    Validasi password
    """
    if not input_password:
        return False
    if config.STRICT_VALIDATION:
        return input_password == config.PASSWORD
    return True


# ============================================================
#  MAIN LOGIN FUNCTION
# ============================================================

def login():
    """
    Fungsi utama login
    Return:
    - True  -> login berhasil
    - False -> login gagal
    """

    attempt = 0

    while attempt < config.MAX_LOGIN_ATTEMPT:
        clear_screen()

        if config.SHOW_LOGO:
            show_logo()

        show_app_info()

        slow_print("Silakan login untuk masuk ke menu utama\n")

        username = input("Username : ")
        password = input("Password : ")

        if validate_username(username) and validate_password(password):
            print()
            print(config.COLOR_GREEN + "✅ LOGIN BERHASIL")
            print("Akses diterima. Memasuki sistem...")
            print(config.COLOR_RESET)
            time.sleep(1.5)
            return True
        else:
            attempt += 1
            print()
            print(config.COLOR_RED + "❌ LOGIN GAGAL")
            print("Username atau Password tidak valid")
            print(f"Sisa percobaan : {config.MAX_LOGIN_ATTEMPT - attempt}")
            print(config.COLOR_RESET)

            time.sleep(config.LOGIN_FAIL_DELAY)

    # Jika gagal terus
    clear_screen()
    print(config.COLOR_RED + "⛔ AKSES DITOLAK")
    print("Terlalu banyak percobaan login gagal")
    print("Sistem dikunci sementara")
    print(config.COLOR_RESET)
    time.sleep(2)
    return False


# ============================================================
#  END OF FILE
# ============================================================
