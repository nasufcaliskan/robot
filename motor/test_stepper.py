import RPi.GPIO as GPIO
import time

from config.pins import (
    MOTOR1_STEP, MOTOR1_DIR,
    MOTOR2_STEP, MOTOR2_DIR
)

# GPIO ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(MOTOR1_STEP, GPIO.OUT)
GPIO.setup(MOTOR1_DIR, GPIO.OUT)
GPIO.setup(MOTOR2_STEP, GPIO.OUT)
GPIO.setup(MOTOR2_DIR, GPIO.OUT)

# PWM nesneleri (Hardware PWM pinleri)
pwm1 = GPIO.PWM(MOTOR1_STEP, 500)  # 500 Hz
pwm2 = GPIO.PWM(MOTOR2_STEP, 500)  # 500 Hz

def run_motor(pwm, dir_pin, direction, freq, duration):
    GPIO.output(dir_pin, direction)
    pwm.ChangeFrequency(freq)
    pwm.start(50)  # %50 duty
    time.sleep(duration)
    pwm.stop()

try:
    print("Motor 1 ileri (3 sn)")
    run_motor(pwm1, MOTOR1_DIR, GPIO.HIGH, 500, 3)
    time.sleep(1)

    print("Motor 1 geri (3 sn)")
    run_motor(pwm1, MOTOR1_DIR, GPIO.LOW, 500, 3)
    time.sleep(1)

    print("Motor 2 ileri (3 sn)")
    run_motor(pwm2, MOTOR2_DIR, GPIO.HIGH, 500, 3)
    time.sleep(1)

    print("Motor 2 geri (3 sn)")
    run_motor(pwm2, MOTOR2_DIR, GPIO.LOW, 500, 3)

except KeyboardInterrupt:
    print("Test durduruldu")

finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
    print("GPIO temizlendi")
