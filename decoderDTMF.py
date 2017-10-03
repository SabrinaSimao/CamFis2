import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
import scipy
import soundfile as sf

import fourier

class decoderDTMF(object):

	def __init__(self):

		self.fs = 44100
		self.loops = 4 

	def decode(self):

		som,Fourier_Transform = self.time_plot(self.loops)

		self.salva_wav(som,'Sound_received.wav') # salva os som
		self.salva_txt(Fourier_Transform,'Tranformada_de_fourier.txt')

		print(Fourier_Transform)



	def salva(self,som,nome_do_arquivo):

		print("salvando")
		thefile = open(nome_do_arquivo, 'w')
		for item in som:
		  thefile.write("%s\n" % item)
		thefile.close()

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

			
			#plota fourier
			plt.figure("abs(Y[k])")
			plt.plot(X,np.abs(Y))

			plt.xlabel('')
			plt.ylabel('')
			plt.grid()
			plt.title('Modulo Fourier audio')

			
			plt.pause(1)


			lista = np.concatenate([lista,som])


		plt.close()

		print(lista)
		Fourier_Transform = scipy.fft(lista)
		#plt.plot(Fourier_Transform)
		time.sleep(10)
		return (lista, Fourier_Transform)



	def reproduz(self,som):
		print("reprodução:")
		print(som)
		sd.play(som, self.fs)
		sd.wait()


decoderDTMF().decode()