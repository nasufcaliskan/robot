import RPi.GPIO as GPIO
import time

from config.pins import (
    MOTOR1_STEP, MOTOR1_DIR,
    MOTOR2_STEP, MOTOR2_DIR
)


class Stepper:
    def __init__(self, pwm_freq=500):
        # 🔴 lgpio için ZORUNLU sıralama
        GPIO.cleanup()                 # eski kilitleri temizle
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Pin setup
        GPIO.setup(MOTOR1_STEP, GPIO.OUT)
        GPIO.setup(MOTOR1_DIR, GPIO.OUT)
        GPIO.setup(MOTOR2_STEP, GPIO.OUT)
        GPIO.setup(MOTOR2_DIR, GPIO.OUT)

        # PWM nesneleri
        self.pwm1 = GPIO.PWM(MOTOR1_STEP, pwm_freq)
        self.pwm2 = GPIO.PWM(MOTOR2_STEP, pwm_freq)

        self.running1 = False
        self.running2 = False

    # =========================
    # HAREKETLER
    # =========================
    def forward(self, freq=600, duration=0.2):
        GPIO.output(MOTOR1_DIR, GPIO.HIGH)
        GPIO.output(MOTOR2_DIR, GPIO.HIGH)
        self._run(freq, duration)

    def backward(self, freq=600, duration=0.4):
        GPIO.output(MOTOR1_DIR, GPIO.LOW)
        GPIO.output(MOTOR2_DIR, GPIO.LOW)
        self._run(freq, duration)

    def turn_left(self, freq=600, duration=0.5):
        GPIO.output(MOTOR1_DIR, GPIO.LOW)
        GPIO.output(MOTOR2_DIR, GPIO.HIGH)
        self._run(freq, duration)

    def turn_right(self, freq=600, duration=0.5):
        GPIO.output(MOTOR1_DIR, GPIO.HIGH)
        GPIO.output(MOTOR2_DIR, GPIO.LOW)
        self._run(freq, duration)

    def stop(self):
        self.stop_all()

    def _run(self, freq, duration):
        self.pwm1.ChangeFrequency(freq)
        self.pwm2.ChangeFrequency(freq)

        self.pwm1.start(50)
        self.pwm2.start(50)

        self.running1 = True
        self.running2 = True

        time.sleep(duration)
        self.stop_all()

    def stop_all(self):
        try:
            self.pwm1.stop()
        except Exception:
            pass

        try:
            self.pwm2.stop()
        except Exception:
            pass

        self.running1 = False
        self.running2 = False

    def cleanup(self):
        self.stop_all()
        time.sleep(0.1)
        GPIO.cleanup()
