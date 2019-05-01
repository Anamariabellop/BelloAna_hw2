import numpy as np 
import matplotlib.pylab as plt
from scipy import fft
from scipy import fftfreq
import mat

#Almacenamiento de datos signal y signalSuma(suma de dos ondas).

datossignal= np.genfromtxt("signal.dat", delimiter=",")
datossuma= np.genfromtxt("signalSuma.dat", delimiter=",")

t= datos[:,0]
senial = datossignal[:,1]
ssuma= datossuma[:,1]




