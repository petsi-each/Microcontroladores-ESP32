print("Piscando o LED :)")

# Importando os módulos necessários
import time
import machine

# Definindo o delay da piscada e o pino que o LED está conectado
delay = 0.5
pino = 15

# Cria um objeto Pin com o pino que o LED tá conectado e define como saída
led=machine.Pin(pino,machine.Pin.OUT)

while True:
    led.on() # Liga o led
    time.sleep(delay) # Delay
    led.off() # Desliga o led
    time.sleep(delay) # Delay