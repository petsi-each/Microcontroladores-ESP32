import machine
from time import sleep_ms

# Link do Wowki: https://wokwi.com/projects/368002143833132033

buzzerPin = 15
delay = 150
duty = 512

buzzer = machine.PWM(machine.Pin(buzzerPin, machine.Pin.OUT), freq=440, duty=0)

# Notas Musicais
E6  = 1319
G6  = 1568
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
D7  = 2349
E7  = 2637
F7  = 2794
G7  = 3136
A7  = 3520

# Melodia do Mario
mario = [
     E7, E7,  1, E7,  1, C7, E7,  1,
     G7,  1,  1,  1, G6,  1,  1,  1,
     C7,  1,  1, G6,  1,  1, E6,  1,
      1, A6,  1, B6,  1,AS6, A6,  1,
     G6, E7,  1, G7, A7,  1, F7, G7,
      1, E7,  1, C7, D7, B6,  1,  1,
     C7,  1,  1, G6,  1,  1, E6,  1,
      1, A6,  1, B6,  1,AS6, A6,  1,
     G6, E7,  1, G7, A7,  1, F7, G7,
      1, E7,  1, C7, D7, B6,  1,  1,
    ]


print("Playing Mario!")
for note in mario:
    buzzer.freq(note)
    buzzer.duty(duty)
    sleep_ms(delay)
sleep_ms(delay*10)
buzzer.deinit()


