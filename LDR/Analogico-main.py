print("LDR Analógico :)")

# Importando os módulos necessários
import machine

# Número do pino na placa no qual o LDR está conectado e valor que define claro e escuro
LDRanalog = 12
valor = 1467

# Para converter nossa entrada digital em analógica, usamos
# o método "ADC" para o objeto de Pin criado no pino conectado na placa
ldr=machine.ADC(machine.Pin(LDRanalog))

while True:
    # Diferente de sensores digitais (que usamos o método value())
    # com os sensores analógicos, utilizamos o método read()
    if ldr.read() > valor:
        print("Tá escuro ->",ldr.read())
    else:
        print("Tá claro ->",ldr.read())

# No LDR, quando tá com menos luz no ambiente, o sinal é mais forte
