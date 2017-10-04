import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import math
import fourier

fs = 44100
tempo = 1
t = np.linspace(0,tempo,fs*tempo)

def Telefone(tx):

    sd.play(tx, fs)
    sd.wait()
    
    plt.close("all")
    plt.title('Send Sound Wave')
    plt.plot(t, tx)
    plt.xlabel('Time')
    plt.ylabel('Sin(t)')
    plt.xlim(0,0.01)
    plt.ylim(-2,2)
    plt.show()

def Fourier(som):
    
    X,Y = fourier.calcFFT(som, fs)
    
    #plota fourier
    plt.figure("abs(Y[k])")
    plt.plot(X,np.abs(Y))
    plt.xlim(0, 2000)
    plt.ylabel('decibeis')
    plt.xlabel('hertz')
    plt.grid()
    plt.title('Modulo Fourier audio')
    plt.show()




