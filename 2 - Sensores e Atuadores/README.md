# 2 - Sensores e Atuadores

São a forma do nosso sistema interagir com o ambiente e suas variáveis. 

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



*Exemplo:*

- Um sensor de iluminação **mede** a iluminação do ambiente
- Um LED acende, **manipulando** (ou mudando) a iluminação do ambiente   

```Aqui colocar aquele fluxograma```


## Sinal digital ou analógico

O sinal **analógico** pode assumir qualquer valor no seu sinal de saída ao longo do tempo,  desde que esteja dentro da sua faixa de operação.

O sinal **digital** pode assumir apenas dois valores no seu sinal de saída ao longo do  tempo, que podem ser interpretados como zero ou um

### ADC (Analog to Digital Converter)
### PWM (Pulse With Modulation)

## Em qual pino conectar no ESP 32?

Pinos que podem agir como analógicos: 0, 2, 4, 12, 13, 14, 15, 25, 26, 27, 32, 33, 34, 35, 36, 39

## Como usar novos sensores e atuadores?

### 1. Como identificar um sensor/atuador específico?

### 2. Como saber as informações desse sensor/atuador? (O que ele faz, como montar o circuito, especificações...)

### 3. Como programar esse sensor/atuador com MicroPython na ESP 32?

## Contribuições e Considerações Finais

Espero que tenha sido útil
Eba, se aprendeu um novo, adiciona aqui pra gente se ajudar
