#!/usr/bin/env python3
# ============================================================
#  MAIN APPLICATION — BOTT (FIXED)
# ============================================================

import sys
import time
import os

# ============================================================
#  FIX IMPORT MODULE (INJECT CONFIG)
# ============================================================
try:
    from module import config as _config
    sys.modules["config"] = _config  # 🔥 FIX UTAMA
    from module.login import login
    from module.menu import menu
    from module.otp_telegram import send_and_verify_otp
    config = _config
except ImportError as e:
    print("⛔ Gagal import module :", e)
    sys.exit(1)

# ============================================================
#  TERMINAL UTILITY
# ============================================================

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

# ============================================================
#  LOGO
# ============================================================

def show_logo():
    clear_screen()
    print(config.COLOR_YELLOW)
    print("        ██████╗  ██████╗ ████████╗████████╗")
    print("        ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝")
    print("        ██████╔╝██║   ██║   ██║      ██║   ")
    print("        ██╔══██╗██║   ██║   ██║      ██║   ")
    print("        ██████╔╝╚██████╔╝   ██║      ██║   ")
    print("        ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ")
    print(config.COLOR_RED + "              B O T T   T E R M I N A L")
    print(config.COLOR_GREEN + "        Secure • Private • Terminal Based")
    print(config.COLOR_RESET)
    time.sleep(1.2)

def exit_app():
    clear_screen()
    print(config.COLOR_RED)
    print("   ██████╗  ██████╗ ████████╗████████╗")
    print("   ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝")
    print("   ██████╔╝██║   ██║   ██║      ██║   ")
    print("   ██╔══██╗██║   ██║   ██║      ██║   ")
    print("   ██████╔╝╚██████╔╝   ██║      ██║   ")
    print("   ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ")
    print(config.COLOR_YELLOW + "        Terima kasih telah menggunakan")
    print(f"              {config.APP_NAME}")
    print(config.COLOR_RESET)
    time.sleep(1.5)
    sys.exit(0)

# ============================================================
#  MAIN FLOW
# ============================================================

def main():
    show_logo()

    if login() is not True:
        exit_app()

    while True:
        pilihan = menu()

        if pilihan == "1":
            clear_screen()
            print(config.COLOR_CYAN + "=========== OTP TELEGRAM ===========" + config.COLOR_RESET)

            nomor = input("Masukkan Nomor : ").strip()
            if not nomor:
                print(config.COLOR_RED + "❌ Nomor tidak boleh kosong" + config.COLOR_RESET)
                time.sleep(1.5)
                continue

            result = send_and_verify_otp(nomor)

            print()
            if result is True:
                print(config.COLOR_GREEN + "✔ Proses OTP berhasil" + config.COLOR_RESET)
            else:
                print(config.COLOR_RED + "✖ Proses OTP gagal" + config.COLOR_RESET)

            input("\nTekan ENTER untuk kembali ke menu...")

        elif pilihan == "0":
            exit_app()
        else:
            print(config.COLOR_YELLOW + "⚠ Menu belum tersedia" + config.COLOR_RESET)
            time.sleep(1)

# ============================================================
#  ENTRY POINT
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
