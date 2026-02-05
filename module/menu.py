# ============================================================
#  MENU MODULE
# ============================================================
#  File       : menu.py
#  Deskripsi  : Menu utama aplikasi terminal
#               dengan logo dan tampilan profesional
#
#  Logo       : BOTT
#  Warna      : MERAH & KUNING
# ============================================================

import os
import time
import config


# ============================================================
#  TERMINAL UTILITY
# ============================================================

def clear_screen():
    os.system("clear")


def pause(message="Tekan ENTER untuk melanjutkan..."):
    input(f"\n{message}")


# ============================================================
#  LOGO MENU
# ============================================================

def show_menu_logo():
    """
    Menampilkan logo BOTT
    Warna : Merah & Kuning
    """
    print(config.COLOR_RED)
    print(" ██████╗  ██████╗ ████████╗████████╗")
    print(" ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝")
    print(" ██████╔╝██║   ██║   ██║      ██║   ")
    print(" ██╔══██╗██║   ██║   ██║      ██║   ")
    print(" ██████╔╝╚██████╔╝   ██║      ██║   ")
    print(" ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ")
    print(config.COLOR_YELLOW)
    print("        🔥 B O T T   T E R M I N A L 🔥")
    print("================================================")
    print(config.COLOR_RESET)


# ============================================================
#  HEADER MENU
# ============================================================

def show_menu_header():
    show_menu_logo()
    print(f"Aplikasi : {config.APP_NAME}")
    print(f"Versi    : {config.APP_VERSION}")
    print("------------------------------------------------")


# ============================================================
#  MENU LIST
# ============================================================

def show_menu_list():
    print(config.COLOR_YELLOW)
    print("[1] Kirim OTP (Telegram)")
    print("[2] Informasi Sistem")
    print("[3] Bantuan")
    print("[0] Keluar")
    print(config.COLOR_RESET)
    print("------------------------------------------------")


# ============================================================
#  MENU VALIDATION
# ============================================================

def validate_menu_choice(choice):
    return choice in ["1", "2", "3", "0"]


# ============================================================
#  MAIN MENU FUNCTION
# ============================================================

def menu():
    while True:
        clear_screen()
        show_menu_header()
        show_menu_list()

        choice = input("Pilih menu : ").strip()

        if validate_menu_choice(choice):
            return choice
        else:
            print()
            print(config.COLOR_RED + "❌ Pilihan menu tidak valid")
            print(config.COLOR_RESET)
            time.sleep(1.5)


# ============================================================
#  MENU INFO
# ============================================================

def show_system_info():
    clear_screen()
    print(config.COLOR_CYAN)
    print("============= INFORMASI SISTEM =============")
    print(config.COLOR_RESET)
    print(f"Nama Aplikasi : {config.APP_NAME}")
    print(f"Versi         : {config.APP_VERSION}")
    print(f"Author        : {config.APP_AUTHOR}")
    print(f"Environment   : {config.APP_ENVIRONMENT}")
    print("--------------------------------------------")
    pause()


def show_help():
    clear_screen()
    print(config.COLOR_CYAN)
    print("=============== BANTUAN =================")
    print(config.COLOR_RESET)
    print("• Login wajib valid")
    print("• Gunakan menu sesuai fungsi")
    print("• OTP dikirim via Telegram")
    print("-----------------------------------------")
    pause()


# ============================================================
#  END OF FILE
# ============================================================
