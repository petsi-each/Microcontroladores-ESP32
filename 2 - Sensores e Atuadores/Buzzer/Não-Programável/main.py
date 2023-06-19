import machine
from time import sleep

buzzerPin = 15
delay = 0.5

buzzer = machine.Pin(buzzerPin, machine.Pin.OUT)

while True:
    buzzer.on()
    sleep(delay)
    buzzer.off()
    sleep(delay)