all: Resultados_hw2.pdf Seniales.pdf Transformadas.pdf Espectrogramas.pdf Senialtemblor.pdf Transformadatemblor.pdf Espectrogramatemblor.pdf

Resultados_hw2.pdf: *.pdf 
	pdflatex Resultados_hw2.tex 

*.pdf: Fourier.py 
	python Fourier.py 
	
*.pdf: python Plots_hw2.py 
	python

datosedificio.dat: a.out
	./a.out

a.out: Edificio.cpp
	g++ Edificio.cpp 



