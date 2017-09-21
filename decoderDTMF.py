import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
import scipy

def salva(som,nome_do_arquivo):
	print("salvando")
	thefile = open(nome_do_arquivo, 'w')
	for item in som:
	  thefile.write("%s\n" % item)

def time_plot(duração):
	plt.ion()
	fs = 44100
	lista =[]

	for tempo in range(duração):
		print("loop:",tempo)
		audio = sd.rec(int(1*fs), fs, channels=1)
		sd.wait()

		som = audio[:,0]

		t = np.linspace(0,1,1*fs)

		plt.clf()
		plt.plot(t,som)
		plt.xlabel('tempo')
		plt.xlabel('sin(t) recebido')
		plt.pause(1)

		lista = np.concatenate([lista,som])

	print(lista)
	Fourier_Transform = scipy.fft(lista)
	return (lista, Fourier_Transform)



def reproduz(som):
	print("reprodução:")
	print(som)
	sd.play(som, fs)
	sd.wait()

som,Fourier_Transform = time_plot(1)

salva(som,'Sound_received.txt') # salva os som
salva(Fourier_Transform,'Tranformada_de_fourier.txt')

print(Fourier_Transform)