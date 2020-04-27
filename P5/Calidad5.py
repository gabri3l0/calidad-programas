"""
Programa:           5
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    29/03/2020
Descripción:        Programa que integra una funcion usando la regla de Simpson
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Base

E = 0.00001 #Base
n = 0 #Base
lista = [] #Base

class ListaC: #Base #Class
    #Funcion de agregar valor de la lista
    def agregar(self,data): #Base #Class #Deleted
        return lista.append(data) #Base #Class #Deleted
    #Funcion para calcular la P
    def calcularP(self,num_seg): #Modified #Class #Deleted
        p = 0 #Modified #Class #Deleted
        for i in range(0,num_seg+1): #Modified #Class #Deleted
        	xi = (x/num_seg)*i #Modified #Class #Deleted
        	intregral = (1 + (xi**2/dof)) #Modified #Class #Deleted
        	integral2 = (intregral**-((dof+1)/2)) #Added #Class #Deleted
        	fx = (integral2*gamma) #Modified #Class #Deleted
        	
        	if(i==0 or i==num_seg): #Modified #Class #Deleted
        		termsData = ((w*1*fx)/3) #Modified #Class #Deleted
        		p += termsData #Modified #Class #Deleted
        	elif (i%2==0): #Added #Class #Deleted
        		termsData = ((w*2*fx)/3) #Added #Class #Deleted
        		p += termsData #Added #Class #Deleted
        	elif (i%2==1): #Added #Class #Deleted
        		termsData = ((w*4*fx)/3) #Added #Class #Deleted
        		p += termsData #Added #Class 
        return p #Added #Class 

l1 = ListaC() #Base

while True: #Base
    try: #Added
        line = input() #Added
        line = line.split() #Added
        l1.agregar(line) #Added
        n += 1 #Added

    except EOFError: #Added
        break #Added

for i in range(n): #Added
	num_seg = 10 #Base
	x = float(lista[i][0]) #Added
	dof = float(lista[i][1]) #Added
	w = x / num_seg #Added

	gamma = math.gamma((dof+1)/2)/(((dof*math.pi)**0.5)*math.gamma(dof/2)) #Added

	pA = 0 #Added
    pE = 1
    

	while (abs(pE-pA)>=E): #Added
        pE = l1.calcularP(num_seg) #Added

		num_seg *= 2 #Added

		w = x / num_seg #Added

		pA = l1.calcularP(num_seg) #Added


	print("0 to x\t\tdof\t\tActual Value") #Added
	print(x,"\t\t",int(dof),"\t\t",round((pA),5)) #Added

