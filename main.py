from motor.stepper import Stepper
import time

robot = Stepper()

try:
    robot.forward(freq=800, duration=2)
    time.sleep(1)

    robot.backward(freq=800, duration=2)
    time.sleep(1)

    robot.turn_left(freq=600, duration=1)
    time.sleep(1)

    robot.turn_right(freq=600, duration=1)

finally:
    robot.cleanup()
