"""
Programa:           7
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    26/04/2020
Descripción:        Programa que 
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Base

E = 0.000001 #Base
# E = 0.0000000000001 #Base
n = 0 #Base
lista = [] #Base

class ListaC: #Base #Class
    #Funcion de agregar valor de la lista
    def agregar(self,data): #Base #Class #Deleted
        return lista.append(data) #Base #Class
    def calcularP(self,dof,x): #Base #Class
        gamma = math.gamma((dof+1)/2)/(((dof*math.pi)**0.5)*math.gamma(dof/2)) #Base #Class

        pA = 1 #Base #Class
        pE = 0 #Base #Class
        num_seg = 5 #Base #Class

        while (abs(pA-pE)>=E): #Base #Class

            num_seg = num_seg * 2 #Base #Class

            w = x / num_seg #Base #Class

            pA = pE #Base #Class

            newW = 0 #Base #Class
            p = 0 #Base #Class
            for i in range(num_seg + 1): #Base #Class

                intregral = (1 + (newW**2/dof)) #Base #Class 

                integral2 = (intregral**-((dof+1)/2)) #Base #Class 

                fx = (integral2*gamma) #Base #Class 

                if(i==0 or i==num_seg): #Base #Class 
                   termsData = (((w/3)*1*fx)) #Base #Class 
                elif (i%2==0): #Base #Class 
                   termsData = (((w/3)*2*fx)) #Base #Class 
                elif (i%2==1): #Base #Class 
                   termsData = (((w/3)*4*fx)) #Base #Class 

                p += termsData #Base #Class
                newW += w #Base #Class
            pE = p #Base #Class
        return pE #Base #Class
    def calcularX(self,rXY,n,rCuadrada): #Base #Class
        top = (abs(rXY)*math.sqrt(n-2)) #Base #Class
        bot = math.sqrt(1-rCuadrada) #Base #Class
        x = top / bot #Base #Class
        return x #Base #Class
    def calcularRigth(self,xK,promX,n): #Base #Class
        top = (xK-promX)**2 #Base #Class
        bot = 0 #Base #Class
        for data in range(n): #Base #Class
            bot += (float(lista[data][testColumna[i][0]])-promX)**2 #Base #Class
        func = math.sqrt(1+(1/n)+(top**2/bot)) #Base #Class
        return func #Base #Class
    def funcionT(sefl,dof,p): #Base #Class
        x = 1  #Base #Class
        d = 0.5 #Base #Class
        pE = 0 #Base #Class
        flag = False #Base #Class
        pE = 0 #Base #Class

        while (abs(pE - p)>E): #Base #Class
            pA = 1 #Base #Class
            num_seg = 5 #Base #Class

            pE = l1.calcularP(dof,x) #Base #Class

            if flag: #Base #Class
                if (p-pE)>0: #Base #Class
                    d /= 2 #Base #Class
                if d == 0: #Base #Class
                    d = 2 #Base #Class

            if pE > p: #Base #Class
                x -= d #Base #Class
            else: #Base #Class
                x += d #Base #Class
            flag = True #Base #Class
        return x #Base #Class
    def desvstd(self,n,y,x,b0,b1): #Base #Class
        sumatoria = 0 #Base #Class
        for data in range(n): #Base #Class
            sumatoria += (float(lista[data][y])-b0-(b1*float(lista[data][x])))**2 #Base #Class
        desvstd = math.sqrt((1/(n-2))*sumatoria) #Base #Class
        return desvstd #Base #Class
#---------------------------------------------------------
    #Funcion de calcular el promedio del test 
    def promedio(self,param1): #Base #Class
        prom = 0 #Base #Class
        suma = 0 #Base #Class
        for x in lista: #Base #Class
            suma += float(x[param1]) #Base #Class
        prom = (suma/n) #Base #Class
        return prom #Base #Class

    #Funcion de calcular la sumatoria del test
    def sumatoria(self,param1): #Base #Class
        suma = 0 #Base #Class
        for x in lista: #Base #Class
            suma += float(x[param1]) #Base #Class
        return suma #Base #Class

    #Funcion de calcular desv estandar de la lista
    def cuadrados(self,param1): #Base #Class
        numeroCuadrado = 0 #Base #Class
        for x in lista: #Base #Class
            numeroCuadrado += float(x[param1])**2 #Base #Class
        return numeroCuadrado #Base #Class

    #Funcion de calcular el conjunto X*Y del test
    def conjunto(self,param1,param2): #Base #Class
        conjuntoXY = 0 #Base #Class
        for x in lista: #Base #Class
            conjuntoXY += float(x[param1])*float(x[param2]) #Base #Class
        return conjuntoXY #Base #Class

    #Funcion de calcular el parametro B1
    def bUno(self,conjuntoXY,n,promX,promY,cuadradoX): #Base #Class
        return ((conjuntoXY-(n*promX*promY))/(cuadradoX-(n*promX**2))) #Base #Class

    #Funcion de calcular el parametro B0
    def bCero(self,promY,bUno,promX): #Base #Class
        return (promY-bUno*promX) #Base #Class
    #Funcion de calcular el coeficiente rXY
    def rXY(self,n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY): #Added #Class
        return ((n*conjuntoXY-sumaX*sumaY)/(math.sqrt(abs((n*cuadradoX-sumaX**2)*(n*cuadradoY-sumaY**2))))) #Base #Class
    #Funcion de calcular el coeficiente r^2
    def rCuadrada(self,rXY): #Base #Class
        return rXY**2 #Base #Class

    #Funcion de calcular el coeficiente yK
    def yK(self,bCero,bUno,xK): #Base #Class
        return bCero+bUno*xK #Base #Class
#---------------------------------------------------------


l1 = ListaC() #Base

while True: #Base
    try: #Base
        line = input() #Base
        if (line.isupper() or line.islower()): #Base
            print('El dataset no esta limpio contiene letras') #Base
            exit(1) #Base
        line = line.split() #Base
        l1.agregar(line) #Base
        n += 1 #Base
    except EOFError: #Base
        break #Base

testColumna = [[1,3],[1,4],[1,2],[1,2]] #Base

for i in range(2): #Base
    bCero = 0 #Base
    bUno = 0 #Base
    rXY = 0 #Base 
    rCuadrada = 0 #Base 
    yK = 0 #Base
    xK = 386 #Base
    n = len(lista) #Base

    l1 = ListaC() #Base

    sumaX = l1.sumatoria(testColumna[i][0]) #Base
    promX = l1.promedio(testColumna[i][0]) #Base

    sumaY = l1.sumatoria(testColumna[i][1]) #Base
    promY = l1.promedio(testColumna[i][1]) #Base

    cuadradoX = l1.cuadrados(testColumna[i][0]) #Base
    cuadradoY = l1.cuadrados(testColumna[i][1]) #Base 

    conjuntoXY = l1.conjunto(testColumna[i][0],testColumna[i][1]) #Base 

    bUno = l1.bUno(conjuntoXY,n,promX,promY,cuadradoX) #Base
    bCero = l1.bCero(promY,bUno,promX) #Base
    rXY = l1.rXY(n,conjuntoXY,sumaX,sumaY,cuadradoX,cuadradoY) #Base 
    rCuadrada = l1.rCuadrada(rXY) #Base 
    yK = l1.yK(bCero,bUno,386) #Base

    x = l1.calcularX(rXY,n,rCuadrada) #Base

    dof = n-2 #Base

    pE = l1.calcularP(dof,x) #Base

    tail = 1-2*pE #Base

    rigth = l1.calcularRigth(xK,promX,n) #Base

    desvstd = l1.desvstd(n,testColumna[i][1],testColumna[i][0],bCero,bUno) #Base


    # p = 0.349991
    p = 0.35 #Base
    t = l1.funcionT(dof,p) #Base

    print('Test ',(i+1)) #Base
    print('rxy',"{:.9f}".format(rXY)) #Base
    print('r^2',"{:.9f}".format(rCuadrada)) #Base
    print('tail area',round(tail,10)) #Base
    print('B0',"{:.9f}".format(bCero)) #Base
    print('B1',"{:.9f}".format(bUno)) #Base
    print('yk',"{:.9f}".format(yK)) #Base
    print('Range',(t*desvstd*rigth)) #Base
    print('UPI',(yK+(t*desvstd*rigth))) #Base
    print('LPI',(yK-(t*desvstd*rigth))) #Base
    print('----') #Base