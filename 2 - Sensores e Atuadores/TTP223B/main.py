print("TTP223B / Touch sensor :)")

# Importando os módulos necessários
import machine

# Número do pino na placa no qual o touch está conectado
touchPino = 4

# Cria um objeto Pin com o pino que o sensor touch tá conectado e define como entrada
touch = machine.Pin(touchPino,machine.Pin.IN)

while True:
    if touch.value() == 1:
        print("Toque")
    else:
        print("Sem toque")