## Projeto 2 Camada Física - 2017.2

Sabrina S.
Paulo Tozzo

## Projeto 2.3

## Modulação

A modulação da amplitude consiste em multiplicar o sinal por uma portadora que tem sua amplitude varialvel usando a formula:
c(t) = Ac*cos(2π*fc*t) a mudulação permite enviar mais de um sinal na mesma onda.


A demodulação consiste em multplicar o sinal recebido pela portadora novamente para desconstruí-lo e achar os sinais originais.

## Portadoras utilizadas

Utilizamos uma frequencia de corte de 3000hz assim a frequencia das portadoras tem que ser maior que o corte, porem ela não pode ultrapasar 22050hz pos nossa frequencia de amostragem é de 44100 e ainda mais as frequencias das portadoras não podem ser proximas se não elas não seram recuperadas, assim foi escolhido as freqncias 7000hz e 1400hz que segue todos esses requisitos.

## Bandas ocupadas

A banda ocupada terá uma frequencia maxima de 22050hz pois o som que tem uma frequencia de 44100hz será dividido em dois para poder ser recuperado


## Graficos da transmição
![](./graficos_transmissor/fourier_da_soma_nao_necessario.png)

![](./graficos_transmissor/fourier_das_mensagens_moduladas.png)

![](./graficos_transmissor/fourier_do_audio_filtrado.png)

![](./graficos_transmissor/fourier_dos_sinais_originais.png)

![](./graficos_transmissor/mensagem_modulada_no_tempo.png)

![](./graficos_transmissor/sinal_da_portadora.png)

![](./graficos_transmissor/sinal_original_no_tempo.png)

## Graficos da recuperação
som recebido
![](./graficos_receptor/som_recebido_no_tempo.png)

fourier do som demodulado
![](./graficos_receptor/fourier_do_som_demodulado.png)

fourier do som recebido
![](./graficos_receptor/fourier_do_som_recebido.png)

som demodulado no tempo
![](./graficos_receptor/som_demodulado_no_tempo.png)

## recuperação
| Sinal Enviado		                 |Sinal Recebido	            |
|--------------------------- ------|----------------------------|
| ![1](imagem_enconder/som_recebido_modulado_1.png)   |![1](imagem_decoder/som_recebido_modulado_2.png)   |
| ![1](imagem_enconder/som_recebido_modulado_2.png)   |![1](imagem_decoder/mensagem_modulada_2.png)   |


sabrina & paulo
