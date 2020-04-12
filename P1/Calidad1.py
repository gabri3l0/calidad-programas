"""
Programa:           1
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    02/02/2020
Descripción:        Programa que obtiene el promedio y desviacion estandar de una serie de numeros
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Added
lista = [] #Added
flag = True #Added
n = 0 #Added

#Clase para lista de valores
class listaC: #Added #class
	#Funcion de agregar valor de la lista
 	def agregar(self,numero): #Added #class
 		return lista.append(numero) #Added #class

	#Funcion de quitar valor de la lista
 	def quitar(self): #Added #class
 		return lista.pop() #Added #class

 	#Funcion de calcular promedio de la lista
 	def promedio(self): #Added #class
 		prom = 0 #Added #class
 		for x in lista: #Added #class
 			prom += x #Added #class
 		prom = (prom/n) #Added #class
 		return prom #Added #class

 	#Funcion de calcular desv estandar de la lista
 	def desviacion(self): #Added #class
 		desv = 0 #Added #class
 		prom = self.promedio() #Added #class

 		for x in lista: #Added #class
 			desv += (x-prom)**2 #Added #class
 		desv = math.sqrt(desv/(n-1)) #Added #class
 		return desv #Added #class


l1 = listaC() #Added

while flag: #Added
	numero = float(input("Ingresa un numero \n")) #Added
	l1.agregar(numero) #Added
	n += 1 #Added
	decision = input("Quieres agregar otro (y/n) \n") #Added
	if decision == "n": #Added
		flag = False #Added


print("Promedio ","%.2f" % l1.promedio()) #Modified
print("Desviacion Estandar ","%.2f" % l1.desviacion()) #Modified