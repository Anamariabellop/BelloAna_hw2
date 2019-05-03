import numpy as np 
import matplotlib.pylab as plt
from scipy import fftpack
from scipy.fftpack import fft, fftfreq


#Almacenamiento de datos signal y signalSuma(suma de dos ondas).

datossignal= np.genfromtxt("signal.dat")
datossuma= np.genfromtxt("signalSuma.dat")

t= datossignal[:,0]
ts=datossuma[:,0]
senial = datossignal[:,1]
ssuma= datossuma[:,1]

#Grafica con dos subplots uno con los datos de signal y otro con el de suma.

plt.figure()

plt.subplot(2,1,1)
plt.plot(t,senial,'c')
plt.title("Senal 1")
plt.xlabel("t(s)")
plt.ylabel("senial")

plt.subplot(2,1,2)
plt.plot(ts,ssuma, 'g')
plt.title("Suma de seniales")
plt.xlabel("t(s)")
plt.ylabel("senial")
plt.subplots_adjust(hspace=0.5)

plt.savefig("Seniales.pdf")

#Haga transformada de fourier de ambas senales con implementacion propia.
N=len(senial)
n=len(ssuma)
x=np.zeros(N)
x2=np.zeros(n)


def TFD(senial):
	coeficientes=[]
	for i in range(len(senial)):
		resultado=0
		for k in range(len(senial)):

			resultado += senial[k]*np.exp(-1j*np.pi*2*k*(i/N))
		coeficientes.append(resultado/N)

	return coeficientes;
		
#grafica de TFD de ambas senales.
dt=t[1]-t[0]
dt2=ts[1]-t[0]
frecuencias= np.fft.fftfreq(N,dt)
frec=np.fft.fftfreq(n,dt2)

plt.figure(figsize=(20,10))

plt.subplot(2,1,1)
plt.plot(frecuencias,TFD(senial), 'c')
plt.title("Transformada de senial 1")
plt.xlabel("freq(Hz")
plt.ylabel("senial")

plt.subplot(2,1,2)
plt.plot(frecuencias,TFD(ssuma), 'g')
plt.title("Transformada suma seniales")
plt.xlabel("freq(Hz)")
plt.ylabel("senial")
plt.subplots_adjust(hspace=0.5)
plt.savefig("Transformadas.pdf")









