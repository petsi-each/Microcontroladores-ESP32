from machine import Pin
import time

pino = 23
presenca = Pin(pino,Pin.IN)

while True:
    if presenca.value():
        print('Tem movimento')
    else:
        print('Não tem movimento')

