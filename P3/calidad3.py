"""
Programa:           3
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    24/02/2020
Descripción:        Programa que obtiene el promedio y desviacion estandar de una serie de numeros
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Base
lista = [] #Base
flag = True #Base
n = 0 #Base

#Clase para lista de valores
class ListaC: #Base #Class
    #Funcion de agregar valor de la lista
    def agregar(self,numero): #Base #Class #Deleted
        return lista.append(numero) #Base #Class #Deleted

    #Funcion de calcular el promedio del test 
    def promedio(self,param1): #Modified #Class #Deleted
        prom = 0 #Modified #Class #Deleted
        suma = 0 #Modified #Class #Deleted
        for x in lista: #Modified #Class #Deleted
            suma += float(x[param1]) #Modified #Class #Deleted
        prom = (suma/n) #Modified #Class #Deleted
        return prom #Modified #Class #Deleted

    #Funcion de calcular la sumatoria del test
    def sumatoria(self,param1): #Added #Class #Deleted
        suma = 0 #Added #Class #Deleted
        for x in lista: #Added #Class #Deleted
            suma += float(x[param1]) #Added #Class #Deleted
        return suma #Added #Class #Deleted

    #Funcion de calcular desv estandar de la lista
    def cuadrados(self,param1): #Added #Class #Deleted
        numeroCuadrado = 0 #Added #Class #Deleted
        for x in lista: #Added #Class #Deleted
            numeroCuadrado += float(x[param1])**2 #Added #Class #Deleted
        return numeroCuadrado #Added #Class #Deleted

    #Funcion de calcular el conjunto X*Y del test
    def conjunto(self,param1,param2): #Added #Class
        conjuntoXY = 0 #Added #Class
        for x in lista: #Added #Class
            conjuntoXY += float(x[param1])*float(x[param2]) #Added #Class
        return conjuntoXY #Added #Class

    #Funcion de calcular el parametro B1
    def bUno(self,conjuntoXY,n,promX,promY,cuadradoX): #Added #Class
        return ((conjuntoXY-(n*promX*promY))/(cuadradoX-(n*promX**2))) #Added #Class

    #Funcion de calcular el parametro B0
    def bCero(self,promY,bUno,promX): #Added #Class
        return (promY-bUno*promX) #Added #Class

    #Funcion de calcular el coeficiente rXY
    def rXY(self,n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY): #Added #Class
        return ((n*conjuntoXY-sumaX*sumaY)/(math.sqrt(abs((n*cuadradoX-sumaX**2)*(n*cuadradoY-sumaY**2))))) #Added #Class

    #Funcion de calcular el coeficiente r^2
    def rCuadrada(self,rXY): #Added #Class
        return rXY**2 #Added #Class

    #Funcion de calcular el coeficiente yK
    def yK(self,bCero,bUno,xK): #Added #Class
        return bCero+bUno*xK #Added #Class


while True: #Added
    try: #Added
        line = input() #Added
        line = line.split() #Added
        lista.append(line) #Added
        n += 1 #Added

    except EOFError: #Added
        break #Added



bCero = 0 #Added
bUno = 0 #Added
rXY = 0 #Added
rCuadrada = 0 #Added
yK = 0 #Added
xK = 386 #Added

l1 = ListaC() #Added

sumaX = l1.sumatoria(0) #Added
promX = l1.promedio(0) #Added

sumaY = l1.sumatoria(2) #Added
promY = l1.promedio(2) #Added

cuadradoX = l1.cuadrados(0) #Added
cuadradoY = l1.cuadrados(2) #Added

conjuntoXY = l1.conjunto(0,2) #Added

bUno = l1.bUno(conjuntoXY,n,promX,promY,cuadradoX) #Added
bCero = l1.bCero(promY,bUno,promX) #Added
rXY = l1.rXY(n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY) #Added
rCuadrada = l1.rCuadrada(rXY) #Added
yK = l1.yK(bCero,bUno,386) #Added


print("{:.3f}".format(bCero),"{:.6f}".format(bUno),"{:.4f}".format(rXY),"{:.4f}".format(rCuadrada),"{:.4f}".format(yK)) #Added


l2 = ListaC() #Added

sumaX = l2.sumatoria(0) #Added
promX = l2.promedio(0) #Added

sumaY = l2.sumatoria(3) #Added
promY = l2.promedio(3) #Added

cuadradoX = l2.cuadrados(0) #Added
cuadradoY = l2.cuadrados(3) #Added

conjuntoXY = l2.conjunto(0,3) #Added

bUno = l2.bUno(conjuntoXY,n,promX,promY,cuadradoX) #Added
bCero = l2.bCero(promY,bUno,promX) #Added
rXY = l2.rXY(n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY) #Added
rCuadrada = l2.rCuadrada(rXY) #Added
yK = l2.yK(bCero,bUno,386) #Added


print("{:.2f}".format(bCero),"{:.6f}".format(bUno),"{:.4f}".format(rXY),"{:.4f}".format(rCuadrada),"{:.4f}".format(yK)) #Added


l3 = ListaC() #Added

sumaX = l3.sumatoria(1) #Added
promX = l3.promedio(1) #Added

sumaY = l3.sumatoria(2) #Added
promY = l3.promedio(2) #Added

cuadradoX = l3.cuadrados(1) #Added
cuadradoY = l3.cuadrados(2) #Added

conjuntoXY = l3.conjunto(1,2) #Added

bUno = l3.bUno(conjuntoXY,n,promX,promY,cuadradoX) #Added
bCero = l3.bCero(promY,bUno,promX) #Added
rXY = l3.rXY(n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY) #Added
rCuadrada = l3.rCuadrada(rXY) #Added
yK = l3.yK(bCero,bUno,386) #Added


print("{:.2f}".format(bCero),"{:.6f}".format(bUno),"{:.4f}".format(rXY),"{:.4f}".format(rCuadrada),"{:.4f}".format(yK)) #Added


l4 = ListaC() #Added

sumaX = l4.sumatoria(1) #Added
promX = l4.promedio(1) #Added

sumaY = l4.sumatoria(3) #Added
promY = l4.promedio(3) #Added

cuadradoX = l4.cuadrados(1) #Added
cuadradoY = l4.cuadrados(3) #Added

conjuntoXY = l4.conjunto(1,3) #Added

bUno = l4.bUno(conjuntoXY,n,promX,promY,cuadradoX) #Added
bCero = l4.bCero(promY,bUno,promX) #Added
rXY = l4.rXY(n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY) #Added
rCuadrada = l4.rCuadrada(rXY) #Added
yK = l4.yK(bCero,bUno,386) #Added


print("{:.2f}".format(bCero),"{:.6f}".format(bUno),"{:.4f}".format(rXY),"{:.4f}".format(rCuadrada),"{:.4f}".format(yK)) #Added
