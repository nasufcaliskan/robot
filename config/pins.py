"""
GPIO Pin Tanımlamaları
Raspberry Pi 5 + DRV8825
BCM NUMARALANDIRMA
"""

# =========================
# STEP MOTORLAR (DRV8825)
# =========================

# Sol Motor
MOTOR1_STEP = 18   # PWM0
MOTOR1_DIR  = 17

# Sağ Motor
MOTOR2_STEP = 19   # PWM1
MOTOR2_DIR  = 27


# =========================
# ULTRASONIC SENSOR (HC-SR04)
# =========================
TRIG = 16
ECHO = 20


# =========================
# I2C (MPU9250)
# =========================
I2C_SDA = 2
I2C_SCL = 3


# =========================
# DURUM LED
# =========================
STATUS_LED = 5
