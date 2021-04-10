#  -*- coding: utf-8 -*-
from re import split

val1 = []
val2 = []


def pedirFrase():
	frase = input("Ingresa la frase: ")
	return frase


def obtener(frase1, nomLista):
	resultado = split('\D+',frase1)
	for i in resultado:
		nomLista.append(i)
	print(nomLista)

contador = 1

while True:
	nomLista = val1
	obtener(pedirFrase(), nomLista)
	contador = contador + 1

	if contador == 2:
		nomLista = val2
		obtener(pedirFrase(), nomLista)
		#val2.pop()
		break

#print(val1)
#new = int(val1) + int(val2)
#print(new)
#print(val2)

premio1 = int(val1[1])*(int(val1[2])/100) +(-(int(val1[3]))*(int(val1[4]) /100))
premio2 = int(val2[1])*(int(val2[2])/100) +(-(int(val2[3]))*(int(val2[4]) /100))

if premio1 > premio2:
	print("la primera frase tiene mas utilidad")
	print(premio1)
else :
	print("la segunda frase tiene mas utilidad")
	print(premio2)

if premio1 == premio2:
	print("Ambas frases presentan la misma utilidad")
	print(premio1)