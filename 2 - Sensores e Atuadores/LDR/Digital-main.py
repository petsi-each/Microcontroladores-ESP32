print("LDR Digital :)")

# Importando os módulos necessários
import machine

# Número do pino na placa no qual o LDR está conectado
LDRdigital = 12

# Cria um objeto Pin com o pino que o LDR tá conectado e define como entrada
ldr=machine.Pin(LDRdigital,machine.Pin.IN)

while True:
    if ldr.value() == 1:
        print("Tá escuro")
    else:
        print("Tá claro")

# No LDR, quando tá com menos luz no ambiente, o sinal é mais forte
