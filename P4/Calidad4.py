"""
Programa:           4
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    08/03/2020
Descripción:        Programa que obtiene el promedio y desviacion estandar de una serie de numeros
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Base
lista = [] #Base
lnLista = [] #Base
flag = True #Base
n = 0 #Base

class ListaC: #Base #Class
    #Funcion de agregar valor de la lista
    def agregar(self,numero): #Base #Class #Deleted
        return lista.append(numero) #Base #Class #Deleted

    #Funcion de agregar la lista ya con log
    def listaLn(self): #Added #Class #Deleted
        for x in lista: #Added #Class #Deleted
            lnLista.append(math.log(int(x[1])/int(x[2]))) #Added #Class #Deleted

    #Funcion de calcular el promedio del programa 
    def promedio(self): #Modified #Class #Deleted
        prom = 0 #Base #Class #Deleted
        suma = 0 #Modified #Class #Deleted
        for x in lnLista: #Added #Class #Deleted
            suma += float(x) #Added #Class #Deleted
        prom = (suma/n) #Modified #Class #Deleted
        return prom #Modified #Class #Deleted

    #Funcion de calcular la varianza del programa 
    def varianza(self,promedio): #Added #Class #Deleted
        sumVarianza = 0 #Added #Class #Deleted
        for x in lnLista: #Added #Class #Deleted
            sumVarianza+=(x-promedio)**2 #Added #Class #Deleted
        return sumVarianza/(n-1) #Added #Class #Deleted


while True: #Added #Deleted
    try: #Added #Deleted
        line = input() #Added
        line = line.split() #Added
        if len(line)==2: #Added 
            flag = False #Added 
            line.append(1) #Added 
        if flag == True: #Added 
            lista.append(line) #Added
        else: #Added 
            if line[2]==1: #Added 
                lista.append(line) #Added 
            else: #Added 
                line.pop(1) #Added 
                line.append(1) #Added 
                lista.append(line) #Added
        n += 1 #Added

    except EOFError: #Added
        break #Added

l1 = ListaC() #Added

l1.listaLn() #Added 
promedio = l1.promedio() #Added 
varianza = l1.varianza(promedio) #Added 
devStrd = math.sqrt(varianza) #Added 

vs=math.exp(promedio-(2*devStrd)) #Added 
s=math.exp(promedio-devStrd) #Added 
m=math.exp(promedio) #Added 
l=math.exp(promedio+devStrd) #Added 
vl=math.exp(promedio+(2*devStrd)) #Added 

print("VS\tS\tM\tL\tVL") #Added 
print("{:.4f}".format(vs),"{:.4f}".format(s),"{:.4f}".format(m),"{:.4f}".format(l),"{:.4f}".format(vl)) #Added 