import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy as np
import scipy
import soundfile as sf
import math

# fs = 44100

# def salva_wav(som,nome_do_arquivo):
# 	print("salvando som em: ",nome_do_arquivo)
# 	sf.write(nome_do_arquivo, som, fs)

# audio = sd.rec(int(3*fs),fs, channels=1)
# sd.wait()

# salva_wav(audio,'m2.wav')
