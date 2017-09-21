# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:22:01 2017

@author: sabri
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import sounddevice as sd
from pynput import keyboard
from tkinter import *
import threading

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


def plot(x):
    plt.plot(t,x)
    plt.show()

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        print(" ")
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        print(" ")

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.KeyCode.from_char(char=9):
        print("Voce apertou o 9")
        x = t9
        sd.play(t9, fs)
        sd.wait()        
        
    if key == keyboard.KeyCode.from_char(char=8):
        print("Voce apertou o 8")
        sd.play(t8, fs)
        sd.wait()
    if key == keyboard.KeyCode.from_char(char=7):
        print("Voce apertou o 7")
        sd.play(t7, fs)
        sd.wait()
    if key == keyboard.KeyCode.from_char(char=6):
        print("Voce apertou o 6")
        sd.play(t6, fs)
        sd.wait()
    if key == keyboard.KeyCode.from_char(char=5):
        print("Voce apertou o 5")
        sd.play(t5, fs)
        sd.wait()
    if key == keyboard.KeyCode.from_char(char=4):
        print("Voce apertou o 4")
        sd.play(t4, fs)
        sd.wait()
    if key == keyboard.KeyCode.from_char(char=3):
        print("Voce apertou o 3")
        sd.play(t3, fs)
        sd.wait()
    if key == keyboard.KeyCode.from_char(char=2):
        print("Voce apertou o 2")
        sd.play(t2, fs)
        sd.wait()
    if key == keyboard.KeyCode.from_char(char=1):
        print("Voce apertou o 1")
        sd.play(t1, fs)
        sd.wait()

    if key == keyboard.KeyCode.from_char(char=0):
        print("Voce apertou o 0")
        sd.play(t0, fs)
        sd.wait()
    if key == keyboard.Key.esc:
        # Stop listener
        return False
print("APERTE ESC PARA SAIR")

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener: listener.join()

