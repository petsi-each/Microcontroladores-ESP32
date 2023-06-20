import machine
from time import sleep_ms

# Link do Wowki: https://wokwi.com/projects/368002143833132033

buzzerPin = 15
delay = 150
duty = 216


buzzer = machine.PWM(machine.Pin(buzzerPin))

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
     E7, E7,  0, E7,  0, C7, E7,  0,
     G7,  0,  0,  0, G6,  0,  0,  0,
     C7,  0,  0, G6,  0,  0, E6,  0,
      0, A6,  0, B6,  0,AS6, A6,  0,
     G6, E7,  0, G7, A7,  0, F7, G7,
      0, E7,  0, C7, D7, B6,  0,  0,
     C7,  0,  0, G6,  0,  0, E6,  0,
      0, A6,  0, B6,  0,AS6, A6,  0,
     G6, E7,  0, G7, A7,  0, F7, G7,
      0, E7,  0, C7, D7, B6,  0,  0,
    ]

while True:
    buzzer.init(freq=440, duty=0)
    print("Playing Mario!")
    for note in mario:
        if note == 0:
            buzzer.duty(0)
        else:
            buzzer.duty(duty)
            buzzer.freq(note)
        sleep_ms(delay)
    sleep_ms(delay*10)
    buzzer.deinit()


