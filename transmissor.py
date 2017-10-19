import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy import signal as sg
import soundfile as sf
import fourier
import math

class transmissor(object):

	def __init__(self):
		self.corte = 2000
		self.fc1 = 3000 #frequencia escolhida arbitrariamente
		self.fc2 = 9000 #frequencia escolhida arbitrariamente
		self.ac1 = 1
		self.ac2 = 1
		self.fs = 44100
		self.tempo1 = 4
		self.tempo2 = 3
		self.t1 = np.linspace(0,self.tempo1,self.fs*self.tempo1)
		self.t2 = np.linspace(0,self.tempo2,self.fs*self.tempo2)
		self.fp1 = self.ac1*np.sin(2*math.pi*self.fc1*self.t1)
		self.fp2 = self.ac2*np.sin(2*math.pi*self.fc2*self.t2)
		
	def transmitir(self):
		m1, fs1 = sf.read('m1.wav')
		#m1 = m1[:,1]

		m2, fs2 = sf.read('m2.wav')
		#m2 = m2[:,1]

		m1f = self.LPF(m1, self.corte, fs1)
		m2f = self.LPF(m2, self.corte, fs2)

		#self.plot_fourier(m1f,fs1)
		#self.plot_fourier(m2f,fs2)

		#self.reproduz(m1f,fs1)
		#self.reproduz(m2f,fs2)
	
		print("Modulacoes: ")
	
		am1 = self.modula1(m1f)
		am2 = self.modula2(m2f)
	
		# self.plot_fourier(self.fp1, fs1)
		# self.plot_fourier(m1f, fs1)
		# self.plot_fourier(am1, fs1)

		#self.plot_fourier(self.fp2, fs2)
		#self.plot_fourier(am2, fs2)
		
		#self.reproduz(am1, fs1)
		#self.reproduz(am2, fs2)
		zero = np.zeros(44100) 
		#Tempo dos audios é diferente, para somar eles, adicionamos 1 segundo de informacao cheia de zeros
		am2_new = np.append(am2, zero)
		soma = am1 + am2_new #somamos ambos sinais modulados

		self.plot_fourier(soma, 44100)
		self.reproduz(soma, 44100)
	
	def modula1(self,som):
		am = som*self.fp1
		return am

	def modula2(self,som):
		am = som*self.fp2
		return am

	def reproduz(self,som,fs):
		print("reprodução...")
		#print(som)
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

transmissor().transmitir()