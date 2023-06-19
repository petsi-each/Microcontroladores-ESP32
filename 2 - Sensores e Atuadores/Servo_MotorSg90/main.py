from machine import Pin,PWM
import time

pino = 25
servoPin = Pin(25,Pin.OUT)
motor = PWM(servoPin,freq = 50)
motor.duty(40)

while True:
    motor.duty(110)
    time.sleep(0.5)
    motor.duty(40)
    time.sleep(0.5)