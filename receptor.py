import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy import signal as sg
import soundfile as sf
import math
import fourier

class receptor(object):

	def __init__(self):

		self.tempo = 4 # tempo de gravação
		self.corte = 3000
		self.fc1 = 7000 #frequencia escolhida arbitrariamente
		self.fc2 = 14000 #frequencia escolhida arbitrariamente
		self.ac1 = 1
		self.ac2 = 1
		self.fs = 44100
		self.tempo1 = 4
		self.tempo2 = 4
		self.t1 = np.linspace(0,self.tempo1,self.fs*self.tempo)
		self.t2 = np.linspace(0,self.tempo2,self.fs*self.tempo)

		self.fp1 = self.ac1*np.sin(2*math.pi*self.fc1*self.t1)
		self.fp2 = self.ac2*np.sin(2*math.pi*self.fc2*self.t2)


	def receive(self):
		lista =[]

		print("gravando...")
		audio = sd.rec(int(self.tempo*self.fs), self.fs, channels=1)
		sd.wait()
		print("Fim da gravacao")
		som = audio[:,0]

		# multiplicar elas portadoras aqui
		m1 = self.fp1 * som
		m2 = self.fp2 * som

		# o som passa pelo filtro passa baixa
		m1 = self.LPF(m1,self.corte,self.fs)
		m2 = self.LPF(m2,self.corte,self.fs)
		print("Reproduzindo...")
		self.reproduz(m1)
		self.reproduz(m2)
		
		self.salva_wav(m1,"m1_recebido.wav",self.fs)
		self.salva_wav(m2,"m2_recebido.wav",self.fs)

		print("Grafico do som recebido no tempo: ")
		#plot dos tempos
		plt.figure("y(t)")
		plt.plot(self.t1[44100:44600],som[44100:44600])
		plt.pause(2)
		plt.close()
		plt.title('y(t) no tempo')

		print("Som demodulado no tempo: ")
		plt.figure("y(t)")
		plt.plot(self.t1,m1)
		plt.plot(self.t2,m2)
		plt.pause(3)
		plt.close()
		plt.title('y(t) recuperado no tempo')

		print("Fourier da soma(som recebido): ")
		self.plot_fourier(som,self.fs) #plot do frequencia
		plt.close()

		print("Foueirers dos sons demodulados: ")
		self.plot_fourier(m1,self.fs)#plot da frequencia do soms separados
		self.plot_fourier(m2,self.fs)

	def plot_fourier(self,som,fs):
		#calcula fourier
		X,Y = fourier.calcFFT(som, fs)
		Y2 = Y
		y_lista = Y2.tolist()
		
		for i in range(len(y_lista)):
			i_db = 10*(math.log10(np.abs(y_lista[i])/25000))
			y_lista[i] = i_db
		
		#plota fourier
		plt.figure("db")
		plt.plot(X,y_lista)
		plt.xlim(0, 22000)
		plt.ylabel('decibeis')
		plt.xlabel('hertz')
		plt.grid()
		plt.title('Decibeis por Hz')

		plt.pause(5)

	def LPF(self,signal, cutoff_hz, fs):
		#####################
		# Filtro
		#####################
		# https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
		nyq_rate = fs/2
		width = 5.0/nyq_rate
		ripple_db = 60.0 #dB
		N , beta = sg.kaiserord(ripple_db, width)
		taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
		return( sg.lfilter(taps, 1.0, signal))

	def salva_wav(self,som,nome_do_arquivo,fs):
		print("salvando som em: ",nome_do_arquivo)
		sf.write(nome_do_arquivo, som, fs)


	def reproduz(self,som):
		print("reprodução:")
		print(som)
		sd.play(som, self.fs)
		sd.wait()


receptor().receive()