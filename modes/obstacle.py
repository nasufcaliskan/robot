import time
import lgpio


class Ultrasonic:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin

        self.chip = lgpio.gpiochip_open(0)

        lgpio.gpio_claim_output(self.chip, self.trig)
        lgpio.gpio_claim_input(self.chip, self.echo)

        lgpio.gpio_write(self.chip, self.trig, 0)
        time.sleep(0.05)

        self.last_distance = 100  # robotun yürüyebilmesi için

    def distance_cm(self):
        # Trigger
        lgpio.gpio_write(self.chip, self.trig, 1)
        time.sleep(0.00001)
        lgpio.gpio_write(self.chip, self.trig, 0)

        start_time = time.time()

        # Echo HIGH bekle (max 5ms)
        while lgpio.gpio_read(self.chip, self.echo) == 0:
            if time.time() - start_time > 0.005:
                return self.last_distance

        pulse_start = time.time()

        # Echo LOW bekle (max 25ms)
        while lgpio.gpio_read(self.chip, self.echo) == 1:
            if time.time() - pulse_start > 0.025:
                return self.last_distance

        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = (pulse_duration * 34300) / 2
        distance = round(distance, 2)

        # mantıksız ölçüm filtre
        if distance < 3 or distance > 300:
            return self.last_distance

        self.last_distance = distance
        return distance

    def close(self):
        lgpio.gpiochip_close(self.chip)
