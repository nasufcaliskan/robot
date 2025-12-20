from motor.stepper import Stepper
import time

robot = Stepper()

print("İleri")
robot.forward(steps=4000, speed=1000)
time.sleep(1)

print("Geri")
robot.backward(steps=4000, speed=1000)
time.sleep(1)

print("Sola dön")
robot.turn_left(steps=2000, speed=1000)
time.sleep(1)

print("Sağa dön")
robot.turn_right(steps=2000, speed=1000)

robot.close()
print("Test bitti")
