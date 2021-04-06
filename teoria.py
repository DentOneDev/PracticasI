#  -*- coding: utf-8 -*-
from re import split
#Los comentarios son por las diferentes modificaciones en el archivo
ganancias = []
ganancias1 = []
resultado = ()

#frase = int(input("a) Ganar $200 con 77% de probabilidad o perder $100 con 23% de probabilidad."))
frase = input("Ingresa la frase 1: ")
#print(frase)

resultado = split(r'\D+', frase)
for i in resultado:
	ganancias.append(i)
	#print(i)
	#print(ganancias)

#frase = int(input("a) Ganar $200 con 77% de probabilidad o perder $100 con 23% de probabilidad."))
frase = input("\nIngresa la frase 2: ")
#print(frase)

resultado = split(r'\D+', frase)
for i in resultado:
	ganancias1.append(i)
	#print(i)
	#print(ganancias1)

#print(ganancias)
#print(ganancias1)
res0 = (int(ganancias[1])*(int(ganancias[2])/100)-int(ganancias[3])*(int(ganancias[4])/100))
#print("\n"+ str(res0))

res1 = (int(ganancias1[1]) * (int(ganancias1[2])/100)-int(ganancias1[3]) * (int(ganancias1[4])/100))
#print("\n"+ str(res1)+"\n")

if res0 >= res1:
	print("\nLa primera frase %s" % str(res0))
	print("La segunda frase %s" % str(res1))
	print("\n\nLa primera frase tiene mas ganancia")
else:
	print("\nLa primera frase %s" % str(res0))
	print("La segunda frase %s" % str(res1))
	print("\n\nLa segunda frase tiene mas ganancia")

if res0 == res1:
	print("Las 2 frases equivalen a  %s" % str(res0))

"""archivo = open("opciones.txt",'r')
for linea in archivo.readlines():
	print(linea)
	archivo.close() 
	Ganar $200 con 61% de probabilidad o perder $600 con 59% de probabilidad.
b) Ganar $300 con 48% de probabilidad o perder $800 con 52% de probabilidad.
"""
"""
if frase == 1:
	print(frase)
	pass
"""

"""
def extraer(texto):
	resultado = split('\D+', text)
	for i in resultado:
		ganancias.append(i)
		print(i)

	for j in resultado:
		resultados0 = (int(variables[1]) * (int(variables[2])/100)-int(variables[3]) * (int(variables[4])/100))	
	resultadosA.append(resultados0)

	return resultados0
	print(resultados0)

	return ganancias[1]
	return ganancias[2]
	return ganancias[3]
	return ganancias[4]

extraer(text)
print(int(variables[1])* 2)

"""

#resultado0 = (int(variables[1]) * (int(variables[2])/100)-int(variables[3]) * (int(variables[4])/100))
#print(resultado0)

#resultadosA.append(resultado0)
#resultadosB.append(resultado1)

#print(resultadosA)
#print(resultadosB)