import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
import scipy
import soundfile as sf
import math
import fourier

class decoderDTMF(object):

	def __init__(self):

		self.fs = 44100
		self.loops = 1

	def decode(self):

		som,Fourier_Transform = self.time_plot(self.loops)

		#som,Fourier_Transform = self.forever_plot()

		self.salva_wav(som,'Sound_received.wav') # salva os som


	def salva_wav(self,som,nome_do_arquivo):
		print("salvando som em: ",nome_do_arquivo)
		sf.write(nome_do_arquivo, som, self.fs)






	def time_plot(self,duração):
		plt.ion()
		lista =[]

		for tempo in range(duração):
			print("loop:",tempo)
			audio = sd.rec(int(1*self.fs), self.fs, channels=1)
			sd.wait()

			som = audio[:,0]
			som = som[9000:] # retira o começo da gravação que sempre esta errada

			t = np.linspace(0,1,1*self.fs)
			t = t[9000:] # retira o começo da gravação que sempre esta errada

			plt.clf()

			#calcula fourier
			X,Y = fourier.calcFFT(som, self.fs)
			Y2 = Y
			y_lista = Y2.tolist()
			
			for i in range(len(y_lista)):
				i_db = 10*(math.log10(np.abs(y_lista[i])/25000))
				y_lista[i] = i_db
			
			#plota fourier
			plt.figure("db")
			plt.plot(X,y_lista)
			plt.xlim(0, 2000)
			plt.ylabel('decibeis')
			plt.xlabel('hertz')
			plt.grid()
			plt.title('Decibeis por Hz')

			
			plt.pause(1)
			plt.close()


			lista = np.concatenate([lista,som])


		Fourier_Transform = scipy.fft(lista)
		#plt.plot(Fourier_Transform)
		time.sleep(1)
		return (lista, Fourier_Transform)


	def reproduz(self,som):
		print("reprodução:")
		print(som)
		sd.play(som, self.fs)
		sd.wait()


decoderDTMF().decode()