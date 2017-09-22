import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
import scipy
import soundfile as sf

def salva(som,nome_do_arquivo):

	print("salvando")
	thefile = open(nome_do_arquivo, 'w')
	for item in som:
	  thefile.write("%s\n" % item)
	thefile.close()

def salva_wav(som,nome_do_arquivo):
	print("salvando som em: ",nome_do_arquivo)
	fs = 44100
	sf.write(nome_do_arquivo, som, fs)



def time_plot(duração):
	plt.ion()
	fs = 44100
	lista =[]

	for tempo in range(duração):
		print("loop:",tempo)
		audio = sd.rec(int(1*fs), fs, channels=1)
		sd.wait()

		som = audio[:,0]
		som = som[9000:]

		t = np.linspace(0,1,1*fs)
		t = t[9000:]

		plt.clf()
		
		#plt.figure(figsize=(10, 10))
		plt.plot(t[1500:2100],som[1500:2100])
		plt.xlabel('tempo')
		plt.ylabel('sin(t) recebido')
		plt.ylim(-0.55,0.55)
		plt.pause(1)

		lista = np.concatenate([lista,som])

	plt.close()

	print(lista)
	Fourier_Transform = scipy.fft(lista)
	#plt.plot(Fourier_Transform)
	time.sleep(10)
	return (lista, Fourier_Transform)



def reproduz(som):
	print("reprodução:")
	print(som)
	sd.play(som, 44100)
	sd.wait()


som,Fourier_Transform = time_plot(2)

salva_wav(som,'Sound_received.wav') # salva os som
salva_txt(Fourier_Transform,'Tranformada_de_fourier.txt')

print(Fourier_Transform)