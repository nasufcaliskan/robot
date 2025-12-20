import sys
import tty
import termios
import time

from motor.stepper import Stepper

# Tek tuş okuma (ENTER'sız)
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key


def main():
    robot = Stepper()

    print("=== UZAKTAN KONTROLLÜ ROBOT ===")
    print("W : İleri")
    print("S : Geri")
    print("A : Sola dön")
    print("D : Sağa dön")
    print("Q : Çikiş")
    print("-----------------------------")

    try:
        while True:
            key = get_key().lower()

            if key == "w":
                robot.forward(freq=800, duration=0.3)

            elif key == "s":
                robot.backward(freq=800, duration=0.3)

            elif key == "a":
                robot.turn_left(freq=600, duration=0.25)

            elif key == "d":
                robot.turn_right(freq=600, duration=0.25)

            elif key == "q":
                print("Çıkılıyor...")
                break

    except KeyboardInterrupt:
        print("\nDurduruldu")

    finally:
        robot.cleanup()


if __name__ == "__main__":
    main()
