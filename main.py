# ============================================================
#  MAIN APPLICATION
# ============================================================
#  File       : main.py
#  Deskripsi  : Entry point aplikasi terminal
#               Menghubungkan:
#               - Login system
#               - Menu utama
#               - OTP Telegram
#
#  Struktur :
#  config.py        -> Konfigurasi pusat
#  login.py         -> Sistem login + logo
#  menu.py          -> Menu utama + logo BOTT
#  otp_telegram.py  -> OTP Telegram (real)
# ============================================================

import sys
import time
import os

# Import module internal
import config
from login import login
from menu import menu, show_system_info, show_help
from otp_telegram import send_and_verify_otp


# ============================================================
#  TERMINAL UTILITY
# ============================================================

def clear_screen():
    """
    Membersihkan layar terminal
    """
    os.system("clear")


def exit_app():
    """
    Keluar dari aplikasi dengan animasi singkat
    """
    clear_screen()
    print(config.COLOR_YELLOW)
    print("========================================")
    print("   Terima kasih telah menggunakan")
    print(f"        {config.APP_NAME}")
    print("========================================")
    print(config.COLOR_RESET)
    time.sleep(1.5)
    sys.exit(0)


# ============================================================
#  MAIN FLOW
# ============================================================

def main():
    """
    Fungsi utama aplikasi
    """
    clear_screen()

    # ============================
    # LOGIN PROCESS
    # ============================
    if not login():
        # Jika login gagal total
        exit_app()

    # ============================
    # MENU LOOP
    # ============================
    while True:
        pilihan = menu()

        # ----------------------------
        # MENU 1 : OTP TELEGRAM
        # ----------------------------
        if pilihan == "1":
            clear_screen()
            print(config.COLOR_CYAN)
            print("=========== OTP TELEGRAM ===========")
            print(config.COLOR_RESET)

            nomor = input("Masukkan Nomor : ").strip()

            if not nomor:
                print()
                print(config.COLOR_RED + "❌ Nomor tidak boleh kosong")
                print(config.COLOR_RESET)
                time.sleep(1.5)
                continue

            result = send_and_verify_otp(nomor)

            print()
            if result:
                print(config.COLOR_GREEN + "✔ Proses OTP selesai dengan sukses")
            else:
                print(config.COLOR_RED + "✖ Proses OTP gagal")
            print(config.COLOR_RESET)

            input("\nTekan ENTER untuk kembali ke menu...")

        # ----------------------------
        # MENU 2 : INFO SISTEM
        # ----------------------------
        elif pilihan == "2":
            show_system_info()

        # ----------------------------
        # MENU 3 : BANTUAN
        # ----------------------------
        elif pilihan == "3":
            show_help()

        # ----------------------------
        # MENU 0 : KELUAR
        # ----------------------------
        elif pilihan == "0":
            exit_app()

        # ----------------------------
        # SAFETY FALLBACK
        # ----------------------------
        else:
            print(config.COLOR_RED + "❌ Terjadi kesalahan menu")
            print(config.COLOR_RESET)
            time.sleep(1)


# ============================================================
#  APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit_app()
    except Exception as e:
        print(config.COLOR_RED)
        print("⛔ ERROR TIDAK TERDUGA")
        print("Detail :", e)
        print(config.COLOR_RESET)
        sys.exit(1)

# ============================================================
#  END OF FILE
# ============================================================
