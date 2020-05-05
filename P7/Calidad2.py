"""
Programa:           2
Nombre:             Gabriel Aldahir Lopez Soto
Fecha de inicio:    16/02/2020
Descripción:        Programa que cuenta la cantidad de lineas de codigo a cierto criterio
Codigo de Honor:    Doy mi palabra que he realizado esta actividad con integridad academica.
"""

baseCont = addedCont = modifiedCont = reusedCont = deletedCont = totalCont = 0 #Added

classParts = {} #Added

#Lee archivo hasta fin de línea
while True: #Added
    try: #Added
        line = input() #Modified
        if(('#Added' in line) & ("'#Added'" not in line)): #Modified
            addedCont += 1 #Added
        if(('#Base' in line) & ("'#Base'" not in line)) : #Added
            baseCont += 1 #Added
        if(('#Modified' in line) & ("'#Modified'" not in line)): #Added
            modifiedCont += 1 #Added
        if(('#Reused' in line) & ("'#Reused'" not in line)): #Added
            reusedCont += 1 #Added
        if(('#Deleted' in line) & ("'#Deleted'" not in line)): #Added
            deletedCont += 1 #Added

        if('class ' in line): #Added
            # print(line)
            splitLine = line.split() #Added
            className = splitLine[1] #Added
            if(className!="'"): #Added
                classParts[className] = {"items" : 0, "size":0} #Added

        if('#Class' in line): #Added
            if(className!="'"): #Added
                classParts[className]["size"] += 1 #Added

            if('def ' in line): #Added
                if(className!="'"): #Added
                    classParts[className]["items"] += 1 #Added
    
        if line.strip(): #Added
            line = line.split() #Added
            if line[0][0] != '#': #Added
                totalCont += 1 #Added

    except EOFError: #Added
        break #Added

for part in classParts: #Added
    print("\n" + 28*"-")#Added
    print("Nombre de la parte: ", part) #Modified
    print("Numero de items: ", classParts[part]["items"]) #Modified
    print("Tamano de la parte: ", classParts[part]["size"]) #Modified
    print(28*"-")#Reused


print("\nTotal de Lineas: ", (totalCont-7),"\n") #Modified
print("Lineas Base: ", baseCont) #Modified
print("Lineas Agregadas: ", addedCont) #Modified
print("Lineas Modificadas: ", modifiedCont) #Modified
print("Lineas Reusadas: ", reusedCont) #Modified
print("Lineas Eliminadas: ", deletedCont) #Modified