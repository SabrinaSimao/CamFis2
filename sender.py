import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import math


fs = 44100
tempo = 0.5
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





