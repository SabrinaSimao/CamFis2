import tkinter as tk
import numpy as np
import math
import sender as snd
import scipy


class Main():

    def iniciar(self):
        self.window.mainloop()
#variaveis
    fs = 44100
    tempo = 1
    t = np.linspace(0,tempo,fs*tempo)

    y1 = np.sin(2*math.pi*697*t)
    y2 = np.sin(2*math.pi*770*t)
    y3 = np.sin(2*math.pi*852*t)
    y4 = np.sin(2*math.pi*941*t)
    x1 = np.sin(2*math.pi*1209*t)
    x2 = np.sin(2*math.pi*1336*t)
    x3 = np.sin(2*math.pi*1477*t)
    x4 = np.sin(2*math.pi*1633*t)

    t1 = y1 + x1
    t2 = y1 + x2
    t3 = y1 + x3
    t4 = y2 + x1
    t5 = y2 + x2
    t6 = y2 + x3
    t7 = y3 + x1
    t8 = y3 + x2
    t9 = y3 + x3
    t0 = y4 + x2
#defs de enviar audios e plotar
    def T1(self):
        snd.Telefone(Main.t1)
        print("Tranformada de fourier: ",scipy.fft(Main.t1))
    def T2(self):
        snd.Telefone(Main.t2)
        print("Tranformada de fourier: ",scipy.fft(Main.t2))
    def T3(self):
        snd.Telefone(Main.t3)
        print("Tranformada de fourier: ",scipy.fft(Main.t3))
    def T4(self):
        snd.Telefone(Main.t4)
        print("Tranformada de fourier: ",scipy.fft(Main.t4))
    def T5(self):
        snd.Telefone(Main.t5)
        print("Tranformada de fourier: ",scipy.fft(Main.t5))
    def T6(self):
        snd.Telefone(Main.t6)
        print("Tranformada de fourier: ",scipy.fft(Main.t6))
    def T7(self):
        snd.Telefone(Main.t7)
        print("Tranformada de fourier: ",scipy.fft(Main.t7))
    def T8(self):
        snd.Telefone(Main.t8)
        print("Tranformada de fourier: ",scipy.fft(Main.t8))
    def T9(self):
        snd.Telefone(Main.t9)
        print("Tranformada de fourier: ",scipy.fft(Main.t9))
    def T0(self):
        snd.Telefone(Main.t0)
        print("Tranformada de fourier: ",scipy.fft(Main.t0))

#interface
    def __init__(self):

        height = 3
        width = 3
      
        self.window = tk.Tk()
        self.window.geometry("60x250")
     
        self.button1 = tk.Button(self.window, text = "1", height = height, width = width)
        self.button1.grid(row = 0, column = 0)
        self.button1.configure(command = self.T1)
        #self.button1.bind("<button0>",1)

        self.button2 = tk.Button(self.window, text = "2", height = height, width = width)
        self.button2.grid(row = 0, column =1)
        self.button2.configure(command = self.T2)

        self.button3 = tk.Button(self.window, text = "3", height = height, width = width)
        self.button3.grid(row = 0, column = 2)
        self.button3.configure(command = self.T3)

        self.button4 = tk.Button(self.window, text = "4", height = height, width = width)
        self.button4.grid(row = 1, column = 0)
        self.button4.configure(command = self.T4)

        self.button5 = tk.Button(self.window, text = "5", height = height, width = width)
        self.button5.grid(row = 1, column = 1)
        self.button5.configure(command = self.T5)

        self.button6 = tk.Button(self.window, text = "6", height = height, width = width)
        self.button6.grid(row = 1, column = 2)
        self.button6.configure(command = self.T6)

        self.button7 = tk.Button(self.window, text = "7", height = height, width = width)
        self.button7.grid(row = 2, column = 0)
        self.button7.configure(command = self.T7)
        
        self.button8 = tk.Button(self.window, text = "8", height = height, width = width)
        self.button8.grid(row = 2, column = 1)
        self.button8.configure(command = self.T8)
        
        self.button9 = tk.Button(self.window, text = "9", height = height, width = width)
        self.button9.grid(row = 2, column = 2)
        self.button9.configure(command = self.T9)
        
        self.button0 = tk.Button(self.window, text = "0", height = height, width = width)
        self.button0.grid(row = 3, column = 1)
        self.button0.configure(command = self.T0)
        #self.button0.bind("<button0>",0)
    
Main().iniciar()