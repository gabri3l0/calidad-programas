"""
Programa:           7
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    26/04/2020
Descripción:        Programa que 
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Base

E = 0.0001 #Base
n = 0 #Base
lista = [] #Base

class ListaC: #Base #Class
    #Funcion de agregar valor de la lista
    def agregar(self,data): #Base #Class #Deleted
        return lista.append(data) #Base #Class #Deleted
    #Funcion para calcular la P
    def calcularP(self,num_seg): #Base #Class #Deleted
        p = 0 #Base #Class #Deleted
        for i in range(0,num_seg+1): #Base #Class
            xi = (x/num_seg)*i #Base #Class
            intregral = (1 + (xi**2/dof)) #Base #Class 
            integral2 = (intregral**-((dof+1)/2)) #Base #Class 
            fx = (integral2*gamma) #Base #Class 
            if(i==0 or i==num_seg): #Base #Class 
               termsData = (((w/3)*1*fx)) #Base #Class 
               p += termsData #Base #Class 
            elif (i%2==0): #Base #Class 
               termsData = (((w/3)*2*fx)) #Base #Class 
               p += termsData #Base #Class 
            elif (i%2==1): #Base #Class 
               termsData = (((w/3)*4*fx)) #Base #Class 
               p += termsData #Base #Class 
        return p #Base #Class
    #Funcion de agregar valor de la lista
    def agregarError(self,data): #Added #Class 
        return error.append(data) #Added #Class 

#---------------------------------------------------------
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
#---------------------------------------------------------


l1 = ListaC() #Base

while True: #Base
    try: #Base
        line = input() #Base
        if (line.isupper() or line.islower()): #Added
            print('El dataset no esta limpio contiene letras') #Added
            exit(1) #Added
        line = line.split() #Base
        l1.agregar(line) #Base
        n += 1 #Base
    except EOFError: #Base
        break #Base

# print("p\t\tdof\t\tActual Value x") #Modified

testColumna = [[1,3],[1,4],[1,2],[1,2]]

print("      r \t r^2 \t  B0 \t\t B1\t\tyk")

for i in range(2): #Base
    bCero = 0 
    bUno = 0 
    rXY = 0 
    rCuadrada = 0 
    yK = 0
    xK = 386
    n = len(lista)

    signo = None #Added
    p = 0

    # d = 0.5 #Added
    # error = [] #Added

    l1 = ListaC()

    sumaX = l1.sumatoria(testColumna[i][0])
    promX = l1.promedio(testColumna[i][0])

    sumaY = l1.sumatoria(testColumna[i][1])
    promY = l1.promedio(testColumna[i][1]) 

    cuadradoX = l1.cuadrados(testColumna[i][0])
    cuadradoY = l1.cuadrados(testColumna[i][1]) 

    conjuntoXY = l1.conjunto(testColumna[i][0],testColumna[i][1]) 

    bUno = l1.bUno(conjuntoXY,n,promX,promY,cuadradoX)
    bCero = l1.bCero(promY,bUno,promX)
    rXY = l1.rXY(n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY) 
    rCuadrada = l1.rCuadrada(rXY) 
    yK = l1.yK(bCero,bUno,386)

    data1 = (abs(rXY)*math.sqrt(n-2))
    data2 = math.sqrt(1-rCuadrada)
    test = data1 / data2

    num_seg = 10 
    dof = n-2
    x = test
    w = x / num_seg

    gamma = math.gamma((dof+1)/2)/(((dof*math.pi)**0.5)*math.gamma(dof/2))

    pA = 0 
    # pE = l1.calcularP(num_seg) 
    pE = 1



    t=0
    while (abs(pE-pA)>E): #Added
        pE = l1.calcularP(num_seg) #Added

        num_seg *= 2 #Added

        w = x / num_seg #Added

        pA = l1.calcularP(num_seg) #Added


    tail = 1-2*pA

    # print(test)
    

    print("{:.9f}".format(rXY),"{:.9f}".format(rCuadrada),"{:.9f}".format(bCero),"{:.9f}".format(bUno),"{:.9f}".format(yK))
    print('Tails',tail)
    print('')
    # break



    # num_seg = num_seg * 2;
    # w = x / num_seg #Base

    # pE = l1.calcularP(num_seg) #Base

    # while (abs(p-pE)>=E): #Base

    #     if signo is None: #Added
    #         if (p-pE)<0: #Added
    #             signo = False #Added
    #         else: #Added
    #             signo = True #Added

    #     signoTemp = signo #Added

    #     if ((p-pE) not in error): #Added
    #         if (p-pE)<0: #Added
    #             signo = False #Added
    #             if (signo != signoTemp): #Added
    #                 d /= 2 #Added
    #             x -= d #Added
    #         if (p-pE)>0: #Added
    #             signo = True #Added
    #             if (signo != signoTemp): #Added
    #                 d /= 2 #Added
    #             x += d #Added
    #         l1.agregarError(p-pE) #Added
    #     else: #Added
    #         if (p-pE)<0: #Added
    #             signo = False #Added
    #             d /= 2 #Added
    #             x -= d #Added
    #         if (p-pE)>0: #Added
    #             signo = True #Added
    #             d /= 2 #Added
    #             x += d #Added

    #     w = x / num_seg #Added

    #     pE = l1.calcularP(num_seg) #Added

    # print(p,"\t\t",int(dof),"\t\t",round(x,5)) #Modified