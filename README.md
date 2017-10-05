## Projeto 2 Camada Física - 2017.2

Sabrina S.
Paulo Tozzo

## Projeto 2.2

## Sinais transmitidos e recebidos
| Tom   | Sinal Enviado		           |Sinal Recebido	            |
|:-----:|----------------------------------|--------------------------------|
|1      | ![1](imagem_enconder/db-1.png)   |![1](imagem_decoder/db_1.png)   |
|2      | ![2](imagem_enconder/db-2.png)   |![2](imagem_decoder/db_2.png)   |
|3      | ![3](imagem_enconder/db-3.png)   |![3](imagem_decoder/db_3.png)   |
|4      | ![4](imagem_enconder/db-4.png)   |![4](imagem_decoder/db_4.png)   |
|5      | ![5](imagem_enconder/db-5.png)   |![5](imagem_decoder/db_5.png)   |
|6      | ![6](imagem_enconder/db-6.png)   |![6](imagem_decoder/db_6.png)   |
|7      | ![7](imagem_enconder/db-7.png)   |![7](imagem_decoder/db_7.png)   |
|8      | ![8](imagem_enconder/db-8.png)   |![8](imagem_decoder/db_8.png)   |
|9      | ![9](imagem_enconder/db-9.png)   |![9](imagem_decoder/db_9.png)   | 
|0      | ![0](imagem_enconder/db.png)     |![0](imagem_decoder/db.png)     |


## Frequências recebidas e a enviadas de cada tom (divergências)

| Tom   | Frequência Enviada (Hz) |Frequência Recebida (Hz)|
|:-----:|:-----------------------:|:----------------------:|
|1      |697, 1209                |695, 1208               |
|2      |697, 1336                |698, 1335               |
|3      |697, 1477                |697, 1480               |
|4      |770, 1209                |771, 1209               |
|5      |770, 1336                |770, 1336               |
|6      |770, 1477                |770, 1477               |
|7      |852, 1209                |851, 1208               |
|8      |852, 1336                |850, 1335               |
|9      |852, 1477                |851, 1477               | 
|0      |941, 1336                |945, 1335               |


## Justificativa dos tempos utilizados
O encoder gasta 1 segundo para enviar o som, tempo suficiente para o receptor captar e perceber o tom escolhido. Menos que isso poderia ser insuficiente, e mais que isso seria desperdicio de energia e muito barulho no ambiente.
O gráfico do Decoder se atualiza a cada 1 segundo, e gasta 1 segundo com o primeiro gráfico (Fourier) e mais 1 segundo com o segundo gráfico (seno). Dessa forma, é um ciclo com um total de 3 segundos. Contudo, ele só capta som no primeiro segundo, que é suficiente para pegar o que o encoder está enviando e tempo suficiente para o usuário mandar outro tom. Menos tempo que isso, o usuário não teria tempo para mandar outras teclas antes de outro gráfico aparecer, e mais tempo que isso captaria muito ruído e gastaria processamento.

# Projeto 2.1

## Geração dos tons

A geração de um som é muito simples, deve-se simplesmente gerar uma onda senoidal, e esta será interpretada como som. 
Usa-se a formula sen(wt) para gerar esta onda, sendo w = 2πf . A frequência é o que diferencia cada nota, e é o principio do passo seguinte; gerar o som das teclas do telefone.

## Frequências que compõem cada tom

No caso dos telefones, uma tabela define a frequência de cada tecla, como pode ser observado na figura 1.

|             |1209 Hz  |1336 Hz  |1477 Hz  |
|:-----------:|:-------:|:-------:|:-------:|
|**697 Hz**   |1        |2        |3        |
|**770 Hz**   |4        |5        |6        |
|**852 Hz**   |7        |8        |9        |
|**941 Hz**   |*        |0        |#        |

Ou seja, a tecla de número 5 é a soma da onda senoidal com frequência 1336Hz e da onda com frequência 770Hz. 

## Gráficos de cada tom (encoder vs decoder):

A escala de algumas imagens ficaram menores que a original por causa da intensidade do som enviado e do próprio microfone do decoder (que esta levemente antigo), porem o gráfico gerado mostra os mesmos padrões dos gráficos originais

| Tecla | Gerado                  	      |Captado     		          |
|:-----:|-------------------------------------|-----------------------------------|
|1      | ![1](imagem_enconder/tecla_1.png)   |![1](imagem_decoder/tecla_1.png)   |
|2      | ![2](imagem_enconder/tecla_2.png)   |![2](imagem_decoder/tecla_2.png)   |
|3      | ![3](imagem_enconder/tecla_3.png)   |![3](imagem_decoder/tecla_3.png)   |
|4      | ![4](imagem_enconder/tecla_4.png)   |![4](imagem_decoder/tecla_4.png)   |
|5      | ![5](imagem_enconder/tecla_5.png)   |![5](imagem_decoder/tecla_5.png)   |
|6      | ![6](imagem_enconder/tecla_6.png)   |![6](imagem_decoder/tecla_6.png)   |
|7      | ![7](imagem_enconder/tecla_7.png)   |![7](imagem_decoder/tecla_7.png)   |
|8      | ![8](imagem_enconder/tecla_8.png)   |![8](imagem_decoder/tecla_8.png)   |
|9      | ![9](imagem_enconder/tecla_9.png)   |![9](imagem_decoder/tecla_9.png)   |
|0      | ![0](imagem_enconder/tecla_0.png)   |![0](imagem_decoder/tecla_0.png)   |

sabrina & paulo