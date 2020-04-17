"""
Programa:           6
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    11/04/2020
Descripción:        Programa que busca el valor de x integrando la funcion t
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Base

E = 0.000000001 #Base
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

print("p\t\tdof\t\tActual Value x") #Modified

for i in range(n): #Base

    signo = None #Added
    num_seg = 10 #Base
    p = float(lista[i][0]) #Modified
    dof = float(lista[i][1]) #Modified
    x = 1 #Added
    d = 0.5 #Added
    error = [] #Added

    gamma = math.gamma((dof+1)/2)/(((dof*math.pi)**0.5)*math.gamma(dof/2)) #Base

    w = x / num_seg #Base

    pE = l1.calcularP(num_seg) #Base

    while (abs(p-pE)>=E): #Base

        if signo is None: #Added
            if (p-pE)<0: #Added
                signo = False #Added
            else: #Added
                signo = True #Added

        signoTemp = signo #Added

        if ((p-pE) not in error): #Added
            if (p-pE)<0: #Added
                signo = False #Added
                if (signo != signoTemp): #Added
                    d /= 2 #Added
                x -= d #Added
            if (p-pE)>0: #Added
                signo = True #Added
                if (signo != signoTemp): #Added
                    d /= 2 #Added
                x += d #Added
            l1.agregarError(p-pE) #Added
        else: #Added
            if (p-pE)<0: #Added
                signo = False #Added
                d /= 2 #Added
                x -= d #Added
            if (p-pE)>0: #Added
                signo = True #Added
                d /= 2 #Added
                x += d #Added

        w = x / num_seg #Added

        pE = l1.calcularP(num_seg) #Added

    print(p,"\t\t",int(dof),"\t\t",round(x,5)) #Modified