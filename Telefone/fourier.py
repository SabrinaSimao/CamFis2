import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window

# Calculate de FFT from a signal
# https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
def calcFFT(signal, fs):

        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

def acha_maximos(X,Y):
	#Acha os dois picos

    n_max = Y.argmax()
    max1 = X[n_max]
    print("Valor Maximo 1:")
    print(max1)

    new_Y = Y

    for i in range(n_max-100, n_max+100):
       new_Y[i] = 0.0j
    
    n_max_2 = new_Y.argmax()
    max2 = X[n_max_2]
    print("Valor Maximo 2:")
    print(max2)

    if max1 > max2:
    	maior = max1
    	menor = max2
    else:
    	maior = max2
    	menor = max1

    return(maior,menor)


def main():

    # Import sound as file
    import soundfile as sf
    y, fs = sf.read('./new_file.wav')

    # Cacula a trasformada de Fourier do sinal
    X, Y = calcFFT(y, fs)

    ## Exibe sinal no tempo
    plt.figure("y[n]")
    plt.plot(y[0:500], 'x')
    plt.grid()
    plt.title('Audio no tempo')

    ## Exibe modulo 
    plt.figure("abs(Y[k])")
    #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.plot(X,np.abs(Y))
    plt.grid()
    plt.title('Modulo Fourier audio')

    ## Exibe fase
    #plt.figure("Fase(Y[k])")
    #plt.plot(X,np.angle(Y))
    #plt.grid()
    #plt.title('Modulo Fourier audio')
    


   


    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()