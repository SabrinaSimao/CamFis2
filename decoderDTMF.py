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
		self.erro = 30 # valor que é admitido como erro da frequencia na hora de receber a onda
		self.loops = 4 

	def decode(self):

		som,Fourier_Transform = self.time_plot(self.loops)

		#som,Fourier_Transform = self.forever_plot()

		self.salva_wav(som,'Sound_received.wav') # salva os som

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


	def acha_tecla(self,frq1,frq2):
		#primera coluna da tabela
		if 1209 - self.erro <= frq1 <= 1209 + self.erro:
			if 697 - self.erro <= frq2 <= 697 + self.erro:
				return "1"
			if 770 - self.erro <= frq2 <= 770 + self.erro:
				return "4"
			if 852 - self.erro <= frq2 <= 852 + self.erro:
				return "7"

		#segunda
		if 1336 - self.erro <= frq1 <= 1336 + self.erro:
			if 697 - self.erro <= frq2 <= 697 + self.erro:
				return "2"
			if 770 - self.erro <= frq2 <= 770 + self.erro:
				return "5"
			if 852 - self.erro <= frq2 <= 852 + self.erro:
				return "8"
			if 941 - self.erro <= frq2 <= 941 + self.erro:
				return "0"


		#terceira
		if 1477 - self.erro <= frq1 <= 1477 + self.erro:
			if 697 - self.erro <= frq2 <= 697 + self.erro:
				return "3"
			if 770 - self.erro <= frq2 <= 770 + self.erro:
				return "6"
			if 852 - self.erro <= frq2 <= 852 + self.erro:
				return "9"

		else:
			return "nenhuma tecla encontrada"





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

			#plt.figure(figsize=(10, 10))
			plt.plot(t[1500:2100],som[1500:2100])
			plt.xlabel('tempo')
			plt.ylabel('sin(t) recebido')
			plt.ylim(-0.55,0.55)

			plt.pause(1)
			plt.close()

			frq1,frq2 = fourier.acha_maximos(X,Y)
			print("Tecla telefonica acionada: ",self.acha_tecla(frq1,frq2))


			lista = np.concatenate([lista,som])


		plt.close()

		print(lista)
		Fourier_Transform = scipy.fft(lista)
		#plt.plot(Fourier_Transform)
		time.sleep(10)
		return (lista, Fourier_Transform)

	def forever_plot(self): # mesma coisa do anterior mas esse roda até crt-c for precionado
		plt.ion()
		lista =[]

		try:
			while True:

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
		except KeyboardInterrupt:
			pass


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