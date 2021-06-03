# Evaluación N° 3
# Diego Sobarzo Licandeo

# Definición de listas
idCarpinteros=[]
maderas=[]
experiencias=[]
trabajos=[]
edades=[]
origenes=[]
antiguedades=[]
opcion=0
# Opciones del menú
while opcion!=4:
    opcion=0
    print("\t\tCarpinteros TOP")
    print("="*50)
    print("1) Registrar Carpintero")
    print("2) Eliminar Carpintero")
    print("3) Ficha Carpintero")
    print("4) Salir")
    while opcion<1 or opcion>4:
        try:
            opcion=int(input("Ingrese opción => "))
            if opcion<1 or opcion>4:
                print("¡La opción ingresada no es válida!")
        except:
            print("¡La opción ingresada debe ser numérica!")
    # Registrar carpintero
    if(opcion==1):
        # El Id del carpintero debe comenzar con @ y dcontener como mínimo 2 caracteres
        while True:          
            idCarpintero=input("Ingrese el ID del carpintero => ")
            if(idCarpintero[0]=="@"):               
                if(len(idCarpintero)>=2):
                    idCarpinteros.append(idCarpintero)
                    break
                else:
                    print("¡El ID del carpintero debe contener mínimo dos caracteres!")
            else:
                print("¡El ID del carpintero debe iniciar con un @!")
        # Madera, madera que lo define
        maderas.append(input("Ingrese madera que lo define => "))
        # Experiencia sólo puede ser ‘Junior’, ‘Senior’ o 'Máster'
        while True: 
            try:
                experiencia=int(input("Ingrese experiencia [1: Junior/ 2:Senior/ 3: Máster] => "))
                if(experiencia==1):
                    experiencias.append("Junior")
                    break
                elif(experiencia==2):
                    experiencias.append("Senior")
                    break
                elif(experiencia==3):
                    experiencias.append("Máster")
                    break
                else:
                    print("¡Experiencia debe ser 1, 2 o 3!")
            except:
                print("¡Experiencia debe ser un valor numérico!")
        # Trabajos, cantidad de trabajos vendidos
        trabajos.append(input("Ingrese cantidad de trabajos vendidos => "))
        # Edad debe ser número entero que se encuentre en el rango 15 y 105
        while True:
            try:
                edad=int(input("Ingrese edad => "))
                if(15<=edad<=105):
                    edades.append(edad)
                    break
                else:
                    print("¡Edad fuera de rango [15 - 105]!")
            except:
                print("¡La edad ingresada debe ser un valor numérico!")
        # Origen solo acepta los caracteres "c" u "o" (c: Chileno / o: Otro) (Mayúscula y minúscula)
        while True: 
            origen=input("Ingrese origen [c: Chileno/ o: Otro] => ")
            if(origen=="c" or origen=="C"):
                origenes.append("Chileno")
                break
            elif(origen=="o" or origen=="O"):
                origenes.append("Otro")
                break
            else:
                print("Origen debe ser 'c' u 'o' en mayúscula o minúsucula")     
        # Antiguedad debe ser un número y como mínimo 2
        while True:
            try:
                antiguedad=int(input("Ingrese antiguedad, tiempo que es carpintero en años => "))
                if(len(str(antiguedad))>=2):
                    antiguedades.append(antiguedad)
                    break
                else:
                    print("¡La antiguedad debe contener mínimo dos dígitos!")
            except:
                print("¡El valor ingresado debe ser numérico!")
    # Eliminar carpintero
    elif(opcion==2):
        while True: 
            idCarpintero=input("Ingrese el ID del carpintero a eliminar => ")
            if(len(idCarpintero)!=0):
                if(len(idCarpinteros)!=0):
                    existe=False
                    for p in range(len(idCarpinteros)):
                        if(idCarpintero==idCarpinteros[p]):
                            existe=True
                            pos=p
                            break
                    if existe:
                        idCarpinteros.pop(p)
                        maderas.pop(p)
                        experiencias.pop(p)
                        trabajos.pop(p)
                        edades.pop(p)
                        origenes.pop(p)
                        antiguedades.pop(p)
                        print("¡Eliminado exitosamente!")   
                    else:
                        print("¡ID de Carpintero no encontrado!")
                else:
                    print("¡ID de Carpintero no encontrado!")
                break
            else:
                print("¡ID de Carpintero no encontrado!")  
    # Ficha Carpintero
    elif(opcion==3):
        while True:
            try:
                antiguedad=int(input("Ingrese experiencia mínima en años de carpinteros a buscar: => "))
                break
            except:
                print("!La experiencia en años ingresada debe ser de tipo numérico!")
        print(f"Listado de Carpinteros con {antiguedad} o más años de experiencia: ")
        for a in range(len(idCarpinteros)):
            if(antiguedad<=antiguedades[a]):
                print(f"{idCarpinteros[a]} | {maderas[a]} | {experiencias[a]} | {trabajos[a]} | {antiguedades[a]} | {origenes[a]}")

        
        
        