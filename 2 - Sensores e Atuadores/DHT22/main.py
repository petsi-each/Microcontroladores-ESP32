import dht
from machine import Pin
from time import sleep

sensorPin = 4
sensor = dht.DHT22(Pin(sensorPin))
delay = 0.5

while True:
    sleep(delay)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Temperatura: %3.1f C' %temp)
    print('Umidade: %3.1f %%' %hum)