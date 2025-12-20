import os
import sys
import time

def clear():
    os.system("clear")

def show_menu():
    clear()
    print("===================================")
    print("        🤖 ROBOT ANA MENÜ 🤖        ")
    print("===================================")
    print("1 - Uzaktan Kontrollü Robot")
    print("2 - Engel Algılayan Robot")
    print("3 - Webcam Kameralı Robot")
    print("4 - Işığı Takip Eden Robot")
    print("5 - Bilgisayar Kontrollü Robot")
    print("6 - Yön Kontrollü Robot")
    print("0 - Çıkış")
    print("===================================")

def run_module(module_name):
    clear()
    print(f"{module_name} çalıştırılıyor...\n")
    time.sleep(1)
    os.system(f"python3 -m {module_name}")

def main():
    while True:
        show_menu()
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            run_module("modes.remote")

        elif secim == "2":
            run_module("modes.obstacle")

        elif secim == "3":
            run_module("modes.webcam")

        elif secim == "4":
            run_module("modes.light_follow")

        elif secim == "5":
            run_module("modes.pc_control")

        elif secim == "6":
            run_module("modes.direction")

        elif secim == "0":
            clear()
            print("Çıkılıyor...")
            sys.exit(0)

        else:
            print("Geçersiz seçim!")
            time.sleep(1)

if __name__ == "__main__":
    main()
