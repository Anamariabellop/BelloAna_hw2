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
def TFD(senial):
	coeficientes=[]
	for i in range(len(senial)):
		resultado=0
		for k in range(len(senial)):

			resultado += senial[k]*np.exp(-1j*np.pi*2*k*i/(len(senial)))
		coeficientes.append(resultado/(len(senial)))

	return coeficientes;
		
#grafica de TFD de ambas senales.
N=len(senial)
n=len(ssuma)
dt=t[1]-t[0]
dt2=ts[1]-t[0]
frecuencias= np.fft.fftfreq(N,dt)
frec=np.fft.fftfreq(n,dt2)

plt.figure(figsize=(10,10))

plt.subplot(2,1,1)
plt.plot(frecuencias,TFD(senial), 'c')
plt.title("Transformada de senial 1")
plt.xlabel("freq(Hz)")
plt.ylabel("senial")

plt.subplot(2,1,2)
plt.plot(frec,TFD(ssuma), 'g')
plt.title("Transformada suma seniales")
plt.xlabel("freq(Hz)")
plt.ylabel("senial")
plt.subplots_adjust(hspace=0.5)
plt.savefig("Transformadas.pdf")

#Espectograma de las dos senales con paquete matplotlib.pyplot.specgram.

plt.figure(figsize=(20,10))

plt.subplot(2,2,1)
plt.specgram(senial)
plt.title("Espectograma 1 senial")
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo(s)")


plt.subplot(2,2,2)
plt.specgram(ssuma)
plt.title("Espectograma suma seniales")
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo(s)")
plt.savefig("Espectogramas.pdf")

#Alamecene los datos de temblor.txt(senial sismica).

sismo= np.genfromtxt("temblor.txt")
senialsismo=sismo[:,1]
tiempo= np.linspace(0,len(sismo))


plt.figure()
plt.plot(tiempo,senialsismo)
plt.xlabel("Tiempo(s)")
plt.ylabel("Senial")
plt.title("Senial Temblor")
plt.savefig("Senialtemblor.pdf")






