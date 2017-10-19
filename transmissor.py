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
		self.corte = 3000
		self.fc1 = 7000 #frequencia escolhida arbitrariamente
		self.fc2 = 14000 #frequencia escolhida arbitrariamente
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

		m2, fs2 = sf.read('m2.wav')

		m1f = self.LPF(m1, self.corte, fs1)
		m2f = self.LPF(m2, self.corte, fs2)
		
		print("Fourier audio filtrado: ")
		self.plot_fourier(m1f,fs1)
		self.plot_fourier(m2f,fs2)
		
		# print("audio filtrados: ")
		# self.reproduz(m1f,fs1)
		# self.reproduz(m2f,fs2)
	
		am1 = self.modula(m1f, self.fp1)
		am2 = self.modula(m2f, self.fp2)

		print("Sinal original no tempo:")
		self.plot_tempo(m1,self.t1,"Sinal original 1")
		self.plot_tempo(m2,self.t2,"Sinal original 2")
		plt.close()
		print("Fourier dos sinais originais: ")

		self.plot_fourier(m1, fs1)
		self.plot_fourier(m2, fs2)
		plt.close()
		print("Portadoras no tempo: ")
		self.plot_portadora(self.fp1,self.t1,"Portadora 1")
		self.plot_portadora(self.fp2,self.t2,"Portadora 2")
		
		print("Mensagens moduladas no tempo: ")
		self.plot_tempo(am1, self.t1, "Modulada 1")
		self.plot_tempo(am2, self.t2, "Modulada 2")

		print("Fourier das mensagens moduladas: ")
		self.plot_fourier(am1,fs1)
		self.plot_fourier(am2,fs2)

		zero = np.zeros(44100) 
		#Tempo dos audios é diferente, para somar eles, adicionamos 1 segundo de informacao cheia de zeros
		am2_new = np.append(am2, zero)
		soma = am1 + am2_new #somamos ambos sinais modulados
		self.salva_wav(soma,"soma.wav",self.fs)
		print("Fourier da soma: ")
		self.plot_fourier(soma, 44100)
		print("Reproduzindo audio somado: ")
		self.reproduz(soma, 44100)
	
	def modula(self,som, fp):
		am = som*fp
		return am

	def salva_wav(self,som,nome_do_arquivo,fs):
		print("salvando som em: ",nome_do_arquivo)
		sf.write(nome_do_arquivo, som, fs)

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

		plt.pause(2)

	def plot_tempo(self, sinal, tempo, nome):
		plt.figure(nome)
		plt.plot(tempo,sinal)
		plt.ylabel("Sinal")
		plt.xlabel("Tempo")
		plt.grid()
		plt.title(nome)

		plt.pause(2)
		plt.close()

	def plot_portadora(self, sinal, tempo, nome):
		plt.figure(nome)
		plt.plot(tempo,sinal)
		plt.ylabel("Sinal")
		plt.xlabel("Tempo")
		plt.ylim(-1.2,1.2)
		plt.xlim(0,0.002)
		plt.title(nome)

		plt.pause(2)
		plt.close()

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