import sounddevice as sd
import matplotlib.pyplot as plt
import time
import numpy

def salva(som):
	thefile = open('Sound_received.txt', 'w')
	for item in som:
	  thefile.write("%s\n" % item)

def time_plot():
	fs = 44100
	duração = 10
	inicio =0
	for tempo in range(duração):
		print("loop:",tempo)
		audio = sd.rec(int(3*fs), fs, channels=1)
		sd.wait()

		som = audio[:,0]

		t = numpy.linspace(0,1,3*fs)

		plt.plot(som,t)
		plt.show(block = False)

		time.sleep(30000)
		plt.close()

fs = 44100
duração = 10
print("recording")
audio = sd.rec(int(duração*fs), fs, channels=1)
sd.wait()

som = audio[:,0]

t = numpy.linspace(0,1,duração*fs)
plt.plot(t,som)
plt.ylabel('some numbers')
plt.show()







# reproduz o som
print("reprodução:")
print(som)
sd.play(som, fs)

# aguarda fim da reprodução
sd.wait()

salva(som) # salva os som