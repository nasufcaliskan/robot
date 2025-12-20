import time
import RPi.GPIO as GPIO

from motor.stepper import Stepper
from config.pins import TRIG, ECHO


class UltrasonicSensor:
    def __init__(self):
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)
        time.sleep(0.2)

    def distance_cm(self, timeout=0.02):
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        start = time.time()

        while GPIO.input(ECHO) == 0:
            if time.time() - start > timeout:
                return None

        pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            if time.time() - pulse_start > timeout:
                return None

        pulse_end = time.time()

        duration = pulse_end - pulse_start
        distance = (duration * 34300) / 2

        return round(distance, 2)


def main():
    robot = Stepper()      # GPIO burada %100 doğru allocate edilir
    sensor = UltrasonicSensor()

    SAFE_DISTANCE = 25
    SPEED = 700

    print("=== ENGEL ALGILAYAN ROBOT ===")

    try:
        while True:
            dist = sensor.distance_cm()

            if dist is None:
                print("Ölçüm yok")
                robot.stop()
                time.sleep(0.1)
                continue

            print(f"Mesafe: {dist} cm")

            if dist > SAFE_DISTANCE:
                robot.forward(freq=SPEED)

            else:
                print("ENGEL!")
                robot.stop()
                time.sleep(0.1)

                robot.backward()
                time.sleep(0.1)

                robot.turn_right()

    except KeyboardInterrupt:
        print("\nDurduruldu")

    finally:
        robot.cleanup()


if __name__ == "__main__":
    main()
