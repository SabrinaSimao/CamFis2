import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy import signal as sg
import soundfile as sf
import fourier
import math

class transmissor(object):

	def transmitir(self):
		m1, fs1 = sf.read('m1.wav')
		#m1 = m1[:,1]

		m2, fs2 = sf.read('m2.wav')
		#m2 = m2[:,1]

		m1_corte = self.LPF(m1, 4000, fs1)
		m2_corte = self.LPF(m2, 4000, fs2)


		self.plot_fourier(m1,fs1)
		self.plot_fourier(m2,fs2)

		self.reproduz(m1_corte,fs1)
		self.reproduz(m2_corte,fs2)


	def reproduz(self,som,fs):
		print("reprodução:")
		print(som)
		sd.play(som, fs)
		sd.wait()

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
		plt.xlim(0, 2000)
		plt.ylabel('decibeis')
		plt.xlabel('hertz')
		plt.grid()
		plt.title('Decibeis por Hz')

		plt.pause(2)



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

transmissor().transmitir()