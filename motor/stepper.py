import lgpio
import time


class Stepper:
    def __init__(self,
                 m1_step=18, m1_dir=17,
                 m2_step=19, m2_dir=27):

        # 🔴 DOĞRU GPIO CHIP
        self.chip = lgpio.gpiochip_open(1)

        self.M1_STEP = m1_step
        self.M1_DIR = m1_dir
        self.M2_STEP = m2_step
        self.M2_DIR = m2_dir

        for pin in (self.M1_STEP, self.M1_DIR,
                    self.M2_STEP, self.M2_DIR):
            lgpio.gpio_claim_output(self.chip, pin)
            lgpio.gpio_write(self.chip, pin, 0)

    def _pulse(self, steps, delay):
        for _ in range(steps):
            lgpio.gpio_write(self.chip, self.M1_STEP, 1)
            lgpio.gpio_write(self.chip, self.M2_STEP, 1)
            time.sleep(delay)
            lgpio.gpio_write(self.chip, self.M1_STEP, 0)
            lgpio.gpio_write(self.chip, self.M2_STEP, 0)
            time.sleep(delay)

    def forward(self, steps=50, speed=500):
        lgpio.gpio_write(self.chip, self.M1_DIR, 1)
        lgpio.gpio_write(self.chip, self.M2_DIR, 1)
        self._pulse(steps, 1 / (2 * speed))

    def backward(self, steps=50, speed=500):
        lgpio.gpio_write(self.chip, self.M1_DIR, 0)
        lgpio.gpio_write(self.chip, self.M2_DIR, 0)
        self._pulse(steps, 1 / (2 * speed))

    def turn_left(self, steps=40, speed=500):
        lgpio.gpio_write(self.chip, self.M1_DIR, 0)
        lgpio.gpio_write(self.chip, self.M2_DIR, 1)
        self._pulse(steps, 1 / (2 * speed))

    def turn_right(self, steps=40, speed=500):
        lgpio.gpio_write(self.chip, self.M1_DIR, 1)
        lgpio.gpio_write(self.chip, self.M2_DIR, 0)
        self._pulse(steps, 1 / (2 * speed))

    def close(self):
        lgpio.gpiochip_close(self.chip)
