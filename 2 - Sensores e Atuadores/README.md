# 2 - Sensores e Atuadores

São a forma do nosso sistema interagir com o ambiente e suas variáveis. 

```Aqui colocar aquele fluxograma```

Os **sensores** são componentes que medem variáveis do ambiente  e convertem essa informação em sinais elétricos, utilizando um transdutor interno, para usar como entrada no controlador. 

**Exemplos de sensores:**
| **Nome do sensor** | **O que é medido** |
|:------------------:|:------------------:|
|   LDR 3mm 3547-2   |    Iluminosidade   |
|        LM35        |     Temperatura    |
|       TTP223B      |        Touch       |
|      TCRT5000      |    Infravermelho   |


Já os **atuadores** manipulam as variáveis do ambiente, agindo como uma saída pro controlador. Ou seja, eles transformam os sinais elétricos em outros tipos de energia para criar alguma ação no ambiente.

**Exemplos de atuadores**
| **Nome do atuador** |          **O que é feito**         |
|:-------------------:|:----------------------------------:|
|     Servo motor     |            Movimentação            |
|       LED RGB       | Emissão de luz de diferentes cores |
|         LED         |           Emissão de luz           |
|     Display OLED    | Emissão de luz em pixels numa tela |
|        Buzzer       |           Emissão de som           |



**Exemplo de sistema**

- Um sensor de iluminação **mede** a iluminação do ambiente
- Um LED acende, **manipulando** (ou mudando) a iluminação do ambiente   

```Aqui colocar uma animaçãozinha se eu conseguir```


## Sinal digital ou analógico

Os sinais de entrada e saída podem ser definidos em **digital** ou **analógico**.

O sinal **digital** pode assumir apenas dois valores no seu sinal, que podem ser interpretados como zero ou um.
****Exemplo:*** um sensor de luminosidade que devolve um 1 caso esteja claro e 0 caso não esteja*

O sinal **analógico** pode assumir qualquer valor no seu sinal dentro de uma faixa de operação. 
****Exemplo:*** um sensor de luminosidade que devolve um valor para a luminosidade do local*

### ADC (Analog to Digital Converter)

Para ter valores analógicos no ESP32 como entrada, nós precisamos utilizar o ADC para converter esse sinais analógicos em digitais a fim de que sejam interpretados pelo controlador.

### DAC (Digital to Analog Converter)

Caso você queira ter valores analógicos como saída, é necessário utilizar o DAC. Ele converte os sinais digitais da placa em sinais analógicos na saída.

### PWM (Pulse With Modulation)

Outra forma é utilizar o PWM, que é uma forma de criar uma saída análoga artificial em um pino digital. Para fazer isso, o sinal do pino é mudado de 0 para 1 rapidamente, por isso, utiliza dois parâmetros: frequência e ciclo de trabalho.


## Em qual pino conectar no ESP 32?

Pinos que podem agir como analógicos: 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39

## Como usar novos sensores e atuadores?

### 1. Como identificar um sensor/atuador específico?

### 2. Como saber as informações desse sensor/atuador? (O que ele faz, como montar o circuito, especificações...)

### 3. Como programar esse sensor/atuador com MicroPython na ESP 32?

## Contribuições e Considerações Finais

Espero que tenha sido útil
Eba, se aprendeu um novo, adiciona aqui pra gente se ajudar
