```Este é o template básico do relatório do curso. Fique à vontade para adicionar mais tópicos, mas preencha todos os tópicos que estão aqui! Este documento está em markdown, mas fique à vontade para criar um documento de texto, desde que contenha os mesmos tópicos. Sugerimos que subam o código e o relatório (como README.md) no github ou, caso não seja possível, código e github como uma pasta zipada no final do curso.```


<p align="center">
  <img src="https://ibb.co/wQ3jfFd" width="300" /><br/>
Nome do projeto <br/>
</p>

<br/>

## :pushpin: Descrição

O que é o seu projeto? Qual o objetivo do sistema?
Não precisa colocar muitas informações técnicas aqui, só deixe sua ideia clara :)

## :robot: Montagem do dispositivo físico

### Lista de materiais

| Quantidade | Nome | Link para referência |
| --- | --- | --- |
| 1 | ESP32 e cabo USB | https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html |
| 4 | Sensor de Toque Touch Capacitivo TTP223B | https://www.baudaeletronica.com.br/sensor-touch-capacitivo-ttp223b.html |
| 4 | Sensor de Temperatura Digital DS18B20 tipo TO92 | https://www.baudaeletronica.com.br/sensor-de-temperatura-digital-ds18b20.html |
| X | Jumpers variados | --- |
| 1 | Protoboard | --- |
| 1 | Resistor 100 ohms | --- |
| 1 | Fonte de alimentação - PowerBank | https://www.americanas.com.br/produto/2706391331 |

### Lista de conexões

| Componente | Pino da placa |
| --- | --- |
| Sensor de Toque A | 21 |
| Sensor de Toque B | 19 |
| Sensor de Toque C | 23 |
| Sensor de Toque D | 22 |
| Sensores de temperatura | 4 |


### Funcionamento dos sensores e atuadores

#### Sensor de temperatura DS18B20 tipo TO92

O DS18B20 é um sensor de temperatural digital que realiza medições na faixa de -55°C até 125°C em graus celsius sem a necessidade de um componente externo para isso. O sensor utiliza o protocolo One-Wire, ou seja, sua comunicação é feita por um único fio de dados (além do VCC e GND), além de possuir um código ID próprio de 64 bits, permitindo a conexão de até 127 sensores num mesmo barramento com endereços diferentes, poupando espaço do projeto. (Especificação técnica: https://www.curtocircuito.com.br/datasheet/sensor/temperatura_DS18B20.pdf)

Este sensor posui precisão de mais ou menos 0,5°C na faixa de medição de -10°C até 85°C. Suas principais características são: 
- Chip: DS18B20;
- Tensão de operação: 3 a 5VDC;
- Consumo: 1,5mA;
- Comunicação: 1 fio;
- Faixa de medição: -55° a 125°C;
- Resolução de saída: 9 a 12 bits (programável);
- Tempo de conversão: 750ms (12-bits);
- Precisão: ±0,5 entre -10°C e 85°C;


#### Sensor de toque TTP223B

O sensor digital de toque TTP223B é de simples funcionamento, mudando o sinal quando há um toque. Sua tensão de operação é entre 2-5, 5V; a saída de estado alto é 0,8V e baixo de 0,3 V. O tempo de resposta é de 220 ms (em estado baixo) e 60 ms (em estado alto), contando com as dimensões de 24 x 24 x 7,2 mm (Especificação técnica: https://files.seeedstudio.com/wiki/Grove-Touch_Sensor/res/TTP223.pdf)

<br/>

### Circuito

<p align="center">
Figura - Diagrama do circuito<br/>
  <img src="https://github.com/Anemaygi/SMAC/blob/master/src/circuitoa.png" width="400" /><br/>
</p>
Informações importantes sobre o circuito, onde colocá-lo, entre outros.
<br/>


## :electric_plug: Funcionamento do sistema

**Não esqueça: adicione um videozinho do sistema funcionando :)**

Liste informações como:
- requisitos do código
- estrutura de arquivos
- qual o objetivo de cada arquivo/pedaço de código
Não precisa ser muito detalhado, apenas o suficiente para que seu código seja entendível!


## :busts_in_silhouette: Contribuir no projeto

### Features implementadas

- [x] Identificação da mudança de posição na cadeira *(exemplo de features que já estão funcionando no projeto)*


### Features para incrementar no projeto

- [ ] Possibilidade do usuário configurar o tempo e a temperatura para os alertas *(exemplo de features que as pessoas podem contribuir no projeto)*



