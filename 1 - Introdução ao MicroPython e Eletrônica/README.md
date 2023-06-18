
```
Em construção - enquanto isso, veja o .pdf :)
```

<p  align="center">
<img  src="../logo.png"  width="150"  /><br/>
Introdução a microcontroladores com ESP32 <br/>
<i>Owlficinas - Aula 2</i>
</p>

<br/>  

# :pushpin: Conceitos

 
**Computação física** é a utilização de variáveis do ambiente no nosso código. É uma mistura de processamento computacional (neste curso, utilizando a placa microcontroladora ESP32) e eletrônica (circuitos, periféricos, sensores e atuadores).

As **placas microcontroladoras** são computadores em um único chip que combinam processador, memória, periféricos de entrada/saída e outros componentes. Eles são amplamente utilizados em sistemas embarcados, brinquedos, controles remotos, robótica e domótica. Ou seja, "computadorzinhos" com menos recursos :)

**Digital** se refere a algo que aceita apenas dois valores: 0 e 1. **Analógico** se refere a qualquer valor entre  um range.

<br/>

# :electric_plug: ESP 32

## Pinagem

Estes termos serão entendidos melhor na Aula 2, mas **ADC** é Analog to Digital Converter, utilizado para utilizar os valores dos sensores analógicos. **DAC** é Digital to Analog converter, que faz o contrário. Por fim, **PWN** é Pulse Width Modulation, uma forma de criar uma saída analógica em um pino digital. 

- Pinos nos quais é possível usar ADC: 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39

- Pinos nos quais é possível usar DAC: 25 e 26

- Pinos nos quais é possível usar PWN: Qualquer saída digital

*P.S.: 34, 35, 36 e 39 apenas recebem entrada*

**VCC** (Voltage Common Collector) é o pino com o maior tensão em relação ao GND. Em relação ao **GND** (Ground), é o pino com tensão 0.

<p  align="center">
<img  src="https://lastminuteengineers.b-cdn.net/wp-content/uploads/iot/ESP32-Pinout.png"  width="450"  />
</p>

:warning: **Atenção!** Alguns pinos podem apresentar comportamento inesperado.

Os pinos verdes são seguros para uso. Os amarelos podem apresentar comportamento imprevisível e é recomendado evitar os vermelhos  

<p  align="center">
<img  src="https://lastminuteengineers.b-cdn.net/wp-content/uploads/iot/ESP32-GPIO-Pins-that-are-Safe-to-Use.png"  width="300"  />
</p>

Para saber mais sobre, [veja aqui](https://lastminuteengineers.com/esp32-pinout-reference/) :)

<br/>

## Botões

### EN

Aperte o botão "EN" para deixar a plaquinha no modo programável ou a resetar. Se a plaquinha travou ou não está respondendo como deveria, aperte o botão "EN", que a reseta, limpando a memória temporária.

### BOOT

Serve para deixar a placa no modo bootavel para adicionar firmware.

<br/>

# :desktop_computer: Programação em MicroPython

O **MicroPython** é uma versão otimizada do Python3, utilizada para microcontroladores e ambientes com poucos recursos.

## Arquivos no MicroPython

O MicroPython possui dois arquivos principais:

**boot.py:**  É executado imediatamente após iniciar o ESP32, utilizado para configurações (como, por exemplo, definição de pins, conexão de rede, etc) antes do código principal começar.

**main.py:** Código principal da sua aplicação! É executado logo após o boot.py

É possível ter outros arquivos e outros scripts na placa, mas invoque-os no main.py!

## Burn o MicroPython na placa

Para usar o MicroPython, é necessário o "burn" em um dispositivo para instalar e integrar o MicroPython no ambiente do ESP32, permitindo que o usuário o use como plataforma de programação.

Aqui há um tutorial completo de como o fazer:

- https://randomnerdtutorials.com/flash-upload-micropython-firmware-esp32-esp8266/

## Programação básica

### Arquivos x REPL

Para colocar código no MicroPython, há duas formas. Você pode uplodear arquivos em sua placa para que eles fiquem permanentes na memória e sejam executados novamente quando a placa reseta. Eles devem seguir os dois arquivos principais explicados previamente.

Outra forma é usar o **REPL**, um ambiente interativo que você pode rodar linhas de código e receber a resposta simultaneamente. É indicado pra testar trechos pequenos de código, mas todos os códigos executados são temporários e se perdem caso resete.

### Importar módulo machine
 
Este módulo possui as funcionalidades e interfaces de hardware com o microcontrolador

```python
import machine
```

### Criar pinos para manipular atuadores ou ler sensores

Para utilizar algum sensor ou atuador no MicroPython, precisamos criar um objeto do tipo "Pin" para manipulá-lo ou lê-lo dentro do código.

#### Criar um pino digital (para sensor ou atuador)
 
- Nome é a variável na qual você vai se referir ao pino no resto do código. Pode ser qualquer um.
- pino é o pino que você conectou o componente na placa
- machine.Pin.IN é para definir se o componente é um sensor
- machine.Pin.OUT é para definir se o componente é um atuador

```python
nome = machine.Pin(pino, machine.Pin.IN/OUT)
```

Exemplo para um sensor de luminosidade no pino 12 da placa:

```python 
luminosidade = machine.Pin(12, machine.Pin.IN)
```

#### Ler o pino digital (sensor)

Basta utilizar o método "value" na variável em que você definiu o pino.

```python
nome.value()
```

#### Mudar o valor do pino digital (atuador)

Há três formas de fazer isso:

:warning: **Atenção!** Alguns sensores/atuadores podem agir de forma inesperada (por exemplo, quando setar o valor para 0, ligar) - leia o datasheet :)

```python
nome.high() # seta o valor para 1 - ligado
nome.low() # seta o valor para 0 - desligado
```

```python
nome.on() # seta o valor para 1 - ligado
nome.off() # seta o valor para 0 - desligado
```

```python
nome.value(1) # seta o valor para 1 - ligado
nome.value(0) # seta o valor para 0 - desligado
```

#### Criar um pino analógico com ADC (para sensor)
 
- Nome é a variável na qual você vai se referir ao pino no resto do código. Pode ser qualquer um.
- pino é o pino que você conectou o componente na placa

```python
nome = machine.ADC(machine.Pin(pino))
```

#### Ler o valor do pino analógico

```python
nome.read()
```


#### Criar um pino analógico com DAC (para atuador)
 
- Nome é a variável na qual você vai se referir ao pino no resto do código. Pode ser qualquer um.
- pino é o pino que você conectou o componente na placa

```python
nome = machine.DAC(machine.Pin(pino))
```


#### Escrever um valor no pino analógico

```python
nome.write(<valor>)
```


## Thonny

Thonny é uma IDE de Python muito simples para iniciantes.

É uma ferramenta na qual é possível ler, manipular, exportar arquivos para sua plaquinha microcontroladora com MicroPython! Não precisa utilizá-la como IDE principal :)

Existem alternativas de terminal, como, por exemplo: [Picocom](https://vorpalhex.com/post/hello-esp32/) (Para REPL) e [Ampy](https://github.com/FNakano/CFA/tree/master/programas/Micropython/ampy) (para manipulação de arquivos da placa)

Link de tutorial para instalação: https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/

### Interface

### Configurações

### Usar REPL

### Enviar arquivos

<br/>

# :robot: Eletrônica básica

## Conceitos

### Circuito elétrico

Por definição, um circuito elétrico é um caminho fechado através do qual a corrente elétrica pode fluir. Ele é composto por uma combinação de componentes e dispositivos eletrônicos.

`adicionar foto`

### Tensão elétrica (V)

É uma diferença potencial entre dois pontos, fazendo uma "pressão" para que os elétrons vão do ponto de maior tensão ao de menor tensão, fornecendo a energia necessária para a corrente fluir

`adicionar foto`

### Corrente elétrica (A)

### Resistência elétrica (Ω)

Um "obstáculo" para o fluxo de corrente elétrica em um circuito. Permite controlar o fluxo de eletricidade nos circuitos para o funcionamento dos componentes

`adicionar foto e explicar da mangueira`

### Lei de Ohm

### Curto circuito

Se a corrente for a mesma e existem alguns pontos que os elétrons possuem mais de um caminho para escolher, mais elétrons vão para o caminho com menor resistência. Se um caminho com resistência muito baixa não-intencional é criado, há um fluxo de corrente MUITO alta e cria um curto circuito

## Componentes

### Protoboard

É uma placa na qual podemos criar circuitos sem a necessidade de soldar

`Complementar + foto`

### Capacitor

É uma "bateria" que pode armazenar e liberar carga elétrica, são usados para armazenamento de engeria, filtragem de sinais, estabilização de tensão, temporização.

` foto`

### Transistor

São dispositivos semicondutores que amplificam ou controlam o fluxo de corrente elétrica em um circuito, como um "interruptor". São usados em portas lógicas!

` foto`

### Diodo

um diodo são componentes que permitem a passagem de corrente em uma só direção. O mais famoso é o LED! Light Emissor Diode :)

`Complementar + foto`

### Resistor

São componentes usados para limitar o fluxo de corrente em um circuito, controlando a resistência elétrica

Possuem diferentes valores definidos por uma tabela de cores. É necessário calcular o melhor resistor para um projeto específico.

`Complementar + foto`

`Foto da tabela`

<br/>

# :books: Desafios

## Desafio 1

No pino 2 do ESP32, há um led embutido! No REPL, faça um blink (ou seja, faça este led piscar - seu valor deve alterar entre 0 e 1 a cada x segundos)

Após fazer no REPL, coloque este código em um arquivo e o envie para a plaquinha para que seja executado sempre que ela executar.

## Desafio 2

Crie um circuito com um led e crie o programa para fazer o blink funcionar

## Desafio 3

Crie um sistema que, quando você aperta o sensor touch, o LED acende.

<br/>

# :open_book: Gabarito

## Desafio 1

```python
import machine
import time
led = machine.Pin(PINO, machine.Pin.OUT) # PINO é qualquer pino que você conectou o LED
while True:
	led.value(1)
	time.sleep(1)
	led.value(0)
	time.sleep(1)
```


## Desafio 2

Crie um circuito com um led e crie o programa para fazer o blink funcionar

## Desafio 3

```python
# PINO1 E PINO2 são quaisquer pinos que você conectou os componentes

import machine
touch = machine.Pin(PINO1, machine.Pin.IN) 
led = machine.Pin(PINO2, machine.Pin.OUT)
while True:
	if touch.value() == 1:
		led.on()
	else:
		led.off()
```

