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
        return lista.append(data) #Base #Class #Deleted
    def calcularP(self,dof,x):
        gamma = math.gamma((dof+1)/2)/(((dof*math.pi)**0.5)*math.gamma(dof/2))

        pA = 1
        pE = 0
        num_seg = 5

        #Inicio del while del pg5 
        while (abs(pA-pE)>=E): #Base

            num_seg = num_seg * 2;

            w = x / num_seg #Base

            pA = pE #WTF

            # pE = l1.calcularP(num_seg,w)
            newW = 0 #WTF
            p = 0
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

                p += termsData
                newW += w   
            # return p #Base #
            pE = p
        return pE
    def calcularX(self,rXY,n,rCuadrada):
        top = (abs(rXY)*math.sqrt(n-2))
        bot = math.sqrt(1-rCuadrada)
        x = top / bot
        return x
    def calcularRigth(self,xK,promX,n):
        top = (xK-promX)**2
        bot = 0
        for data in range(n):
            bot += (float(lista[data][testColumna[i][0]])-promX)**2
        func = math.sqrt(1+(1/n)+(top**2/bot))
        return func
    def funcionT(sefl,dof,p):
        x = 1 
        d = 0.5
        pE = 0
        flag = False
        pE = 0

        #Inicio while pg 6
        while (abs(pE - p)>E): #Base
            pA = 1
            num_seg = 5  

        #Inicio del while del pg5 
            pE = l1.calcularP(dof,x)
        #Fin del while del pg5 

            if flag:
                if (p-pE)>0:
                    d /= 2
                if d == 0:
                    d = 2

            if pE > p:
                x -= d
            else:
                x += d
            flag = True
        return x
    def desvstd(self,n,y,x,b0,b1):
        sumatoria = 0
        for data in range(n):
            sumatoria += (float(lista[data][y])-b0-(b1*float(lista[data][x])))**2
        desvstd = math.sqrt((1/(n-2))*sumatoria)
        return desvstd
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

    x = l1.calcularX(rXY,n,rCuadrada)

    dof = n-2

    pE = l1.calcularP(dof,x)

    tail = 1-2*pE

    rigth = l1.calcularRigth(xK,promX,n)

    desvstd = l1.desvstd(n,testColumna[i][1],testColumna[i][0],bCero,bUno)


    # p = 0.349991
    p = 0.35
    t = l1.funcionT(dof,p)

    print('Test ',(i+1))
    print('rxy',"{:.9f}".format(rXY))
    print('r^2',"{:.9f}".format(rCuadrada))
    print('tail area',round(tail,10))
    print('B0',"{:.9f}".format(bCero))
    print('B1',"{:.9f}".format(bUno))
    print('yk',"{:.9f}".format(yK))
    print('Range',(t*desvstd*rigth))
    print('UPI',(yK+(t*desvstd*rigth)))
    print('LPI',(yK-(t*desvstd*rigth)))
    print('----')