"""
Programa:           6
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    11/04/2020
Descripción:        Programa que busca el valor de x integrando la funcion t
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

import math #Base

E = 0.000000000001 #Base
n = 0 #Base
lista = [] #Base

class ListaC: #Base #Class
    #Funcion de agregar valor de la lista
    def agregar(self,data): #Base #Class #Deleted
        return lista.append(data) #Base #Class #Deleted
    def calcularP(self,num_seg,w): #Base #Class #Deleted
        newW = 0 #Added
        p= 0 #Added
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

            p += termsData #Added
            newW += w #Added
        return p #Base #Class

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

    p = float(lista[i][0]) #Modified
    dof = float(lista[i][1]) #Modified
    x = 1 #Added
    d = 0.5 #Added
    pE = 0 #Added
    flag = False #Added  

    gamma = math.gamma((dof+1)/2)/(((dof*math.pi)**0.5)*math.gamma(dof/2)) #Base

    while (abs(pE - p)>E): #Base
        pA = 1 #Added
        num_seg = 5 #Added

        while (abs(pA-pE)>=E): #Base

            num_seg = num_seg * 2 #Added

            w = x / num_seg #Base

            pA = pE #Added

            pE = l1.calcularP(num_seg,w) #Added

        if flag: #Added
            if (p-pE)>0: #Added
                d /= 2 #Added
            if d == 0: #Added
                d = 2 #Added

        if pE > p: #Added
            x -= d #Added
        else: #Added
            x += d #Added
        flag = True #Added

    print(p,"\t\t",int(dof),"\t\t",x) #Modified