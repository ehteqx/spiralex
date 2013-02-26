#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nella prima riga viene definita la directory radice virtuale di esecuzione dell'interprete Python, in compatibilità con gli ambienti Linux-based (per garantire una effettiva compatibilità cross-platform)
# Nella seconda riga viene definita la codifica del testo sorgente (questo documento) come UTF-8 (necessario per utilizzare caratteri accentati e peculiarità della lingua italiana)
from pylab import * # Vengono importati tutti i sottomoduli del modulo "pylab" (necessario al funzionamento corretto del programma)
from numpy import * # Vengono importati tutti i sottomoduli del modulo "numpy" (necessario al funzionamento corretto del programma)
# INIZIO DEL CODICE VERO E PROPRIO #
# Definizione dell'header dello script:
intro = """
==========================================================================================================================
### SPIRALEX Lite v. 1.2c -- A simple linear-spirals plotter ###
 
Code written in Python 2.7.3 for Python(x,y) using "Notepad++ v6.3" on a "Windows 7 SP1 x64 Home Premium" environment
(C)2013 EMANUELE BALLARIN & GAMMADECAY DEVELOPEMENT - All rights reserved (email: ehteqx@gmail.com)
 
==========================================================================================================================
"""
print (intro) # Stampa l'introduzione
# Definizione delle variabili e delle funzioni del programma:
# Istruzione "while-try-except"
while True: # Fino a quando...
  try: # ... non viene inserito...
		giri = int(raw_input("Inserire il numero di giri che deve fare la spirale. Inserire un numero intero. Giri: ")) # ... un input che sia un numero intero
		break # ... (e in tal caso il software procede)
	except ValueError: # ... viene richiesto nuovamente il numero...
		print "L'input inserito non è un numero intero! Inserire un numero intero valido..." # ... e stampato un messaggio di errore.
# Algoritmo di plotting della spirale, dato il numero di giri:
t = linspace(0, giri*pi, 5000) # Viene definito lo spazio lineare numerico del parametro t
x = t*cos(t) # Viene definito lo spazio lineare delle coordinate parametrice (in funzione di t) sull'asse x dei punti della spirale
y = t*sin(t) # Viene definito lo spazio lineare delle coordinate parametrice (in funzione di t) sull'asse y dei punti della spirale
clf() # Viene elaborato uno spazio vuoto piano
grid() # Viene stampata una griglia sullo sfondo del grafico
axis('equal') # Vengono fissati gli assi come equilateri, monometrici ed ortogonali
plot(x,y,'b') # Viene elaborato il grafico della spirale, di colore blu
show() # Viene plottato il grafico e visualizzato
