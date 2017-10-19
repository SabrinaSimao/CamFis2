import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
import scipy
import soundfile as sf
import math
import fourier

class receptor(object):

	def __init__(self):

		self.tempo = 3

		self.fc1 = 500 #frequencia escolhida arbitrariamente
		self.fc2 = 800 #frequencia escolhida arbitrariamente
		self.ac1 = 100
		self.ac2 = 200
		self.t1 = np.linspace(0,1,self.fs*self.tempo1)
		self.t2 = np.linspace(0,1,self.fs*self.tempo2)

		self.fp1 = self.ac1*np.sin(2*math.pi*self.fc1*self.t1)
		self.fp2 = self.ac2*np.sin(2*math.pi*self.fc2*self.t2)


	def receive(self,fs):
		lista =[]

		audio = sd.rec(int(self.tempo*fs), fs, channels=1)
		sd.wait()

		som = audio[:,0]

		t = np.linspace(0,1,self.tempo*fs)

		# multiplicar elas portadoras aqui
		m1 = fp1 * som
		m2 = fp2 * som

		m1 = LPF(m1,4000,44100)
		m2 = LPF(m2,4000,44100)

		reproduz(m1,44100)
		reproduz(m2,44100)




		salva_wav(m1,"m1_recebido",fs)
		salva_wav(m2,"m2_recebido",fs)

		plt.figure("y(t)")
		plt.plot(t,som)
		plt.title('y(t) no tempo')

		plt.pause(1.5)


		plt.figure("y(t)")
		plt.plot(t,m1)
		plt.plot(t,m2)
		plt.title('y(t) recuperado no tempo')

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
		sd.play(som, fs)
		sd.wait()


decoderDTMF().decode()