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

		m1 = self.LPF(m1,self.corte,self.fs)
		m2 = self.LPF(m2,self.corte,self.fs)

		self.reproduz(m1)
		self.reproduz(m2)

		self.salva_wav(m1,"m1_recebido.wav",self.fs)
		self.salva_wav(m2,"m2_recebido.wav",self.fs)

		# plt.figure("y(t)")
		# plt.plot(self.t1,som)
		# plt.title('y(t) no tempo')


		# plt.figure("y(t)")
		# plt.plot(self.t1,m1)
		# plt.plot(self.t2,m2)
		# plt.title('y(t) recuperado no tempo')

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