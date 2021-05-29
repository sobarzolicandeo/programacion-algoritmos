#crear listas
propietarios=[]
ruts=[]
fonos=[]
correos=[]
patentes=[]
annios=[]
combustibles=[]
puertas=[]
transmisiones=[]
colores=[]
kilometrajes=[]
preciosventas=[]
opcion=0
while opcion!=5:
    opcion=0
    print("\t\tMenú Venta de Autos PGY1121")
    print("="*60)
    print("1. Agregar auto")
    print("2. Mostrar auto")
    print("3. Modificar")
    print("4. Vender Auto ")
    print("5. Salir")
    while opcion<1 or opcion>5:
        try:
            opcion=int(input("Opción=> "))
            if opcion<1 or opcion>5:
                print("Opción NO Válida!!")
        except:
            print("Opción es numérica!!!")
    if(opcion==1):#Agregar auto
        #Validaciones
        propietarios.append(input("Ingrese nombre => "))
        #Rut debe ser como mínimo 5000000 y no más de 21000000
        while True:
            try:
                rut=int(input("Ingrese RUT del propietario => "))
                if(5000000<=rut<=21000000):
                    ruts.append(rut)
                    break
                else:
                    print("Rut Fuera de rango [5000000 - 21000000]!!")
            except:
                print("RUT es un número!!!")
        #El teléfono debe tener 9 dígitos
        while True: 
            fono=input("Ingrese N° de contacto => ")
            if(len(fono)==9):
                fonos.append(fono)
                break
            else:
                print("Fono debe tener 9 dígitos!!")
        #Correo debe tener ‘@’, ‘.’ y como mínimo 6 dígitos
        contA=contPoint=0
        while contA!=1 or contPoint!=1:            
            correo=input("Ingrese su direccicón de Correo => ")
            if(len(correo)>=6):                
                for x in correo:
                    if(x=="@"):
                        contA+=1
                    if(x=="."):
                        contPoint+=1
                if(contA!=1 or contPoint!=1):
                    print("Correo Formato no válido")
                    contA=contPoint=0
            else:
                print("Largo mínimo del correo es 6!!")
        correos.append(correo)
        #La patente debe tener 6 dígitos y debe ser única.
        while True: 
            patente=input("Ingrese patente => ")
            if(len(patente)==6):
                if(len(patentes)!=0):
                    existe=False
                    for p in range(len(patentes)):
                        if(patente==patentes[p]):
                            existe=True
                            break
                    if existe:
                        print("Patente ya existe!!")  
                    else:
                        patentes.append(patente)
                else:
                    patentes.append(patente)
                break
            else:
                print("Formato patente NO válido!!")
        #Combustible solo puede ser ‘Diesel’ o ‘Kerosene’
        while True: 
            try:
                combustible=int(input("Ingrese combustible [1: Diesel/ 2:Kerosene] => "))
                if(combustible==1):
                    combustibles.append("Diesel")
                    break
                elif(combustible==2):
                    combustibles.append("Kerosene")
                    break
                else:
                    print("Combustible debe ser 1 ó 2")
            except:
                print("Sólo números!!")            
        #Cantidad de puertas debe ser como mínimo 2
        while True: 
            try:
                puerta=int(input("Ingrese Cantidad de puertas => "))
                if(puerta>=2):
                    puertas.append(puerta)
                    break
                else:
                    print("Puerta debe ser como mínimo 2!!")
            except:
                print("Puertas es numérico!!!")
        #Tipo de Transmisión ‘M’ o ‘A’  
        while True:
            transmision=input("Ingrese Tipo de Transmisión [A: automático/ M: mecánico] => ")
            if(transmision.lower()=="a" or transmision.lower()=="m"):
                transmisiones.append(transmision)
                break
            else:
                print("Transmisión solo puede ser A ó M!!")  
        colores.append(input("Ingrese Color del auto => "))
        while True:
            try:
                kilometrajes.append(int(input("Ingrese kilometraje del vehículo => ")))
                break
            except:
                print("Kms. es numérico!!")
        while True:
            try:
                annios.append(int(input("Ingrese año del vehículo => ")))
                break
            except:
                print("Año es numérico!!")
        while True:
            try:
                preciosventas.append(int(input("Ingrese valor de venta del vehículo => $")))
                break
            except:
                print("Precio es numérico!!")
        print("Vehículo ingresado con Exito!!")                        
    elif(opcion==2):#Mostrar auto
        while True:
            try:
                annio=int(input("Ingrese año de búsqueda => "))
                break
            except:
                print("Año es un número!!")
        print("Listado de Autos ")
        for a in range(len(propietarios)):
            if(annio<=annios[a]):
                print(f"{patentes[a]} | {combustibles[a]} | {propietarios[a]} | {puertas[a]} | {kilometrajes[a]} | {preciosventas[a]}")
    elif(opcion==3):        
        if(len(patentes)!=0):
            while True:
                try: 
                    op=int(input("1: Modifica Precio / 2: Modifica KM\nIngrese su opción => "))
                    if(op==1 or op==2):
                        break
                    else:
                        print("Opción es 1 ó 2!")
                except:
                    print("Es un número!!")  
            while True: 
                patente=input("Ingrese patente => ")
                if(len(patente)==6):
                    existe=False
                    for p in range(len(patentes)):
                        if(patente==patentes[p]):
                            existe=True
                            pos=p
                            break
                    if existe:
                        if(op==1):
                            while True:
                                try:
                                    newPrecio=(int(input("Ingrese nuevo valor => $")))
                                    preciosventas[p]=newPrecio
                                    break
                                except:
                                    print("Precio es numérico!!") 
                        else:
                            while True:
                                try:
                                    km=(int(input("Ingrese nuevo kilometraje del vehículo => ")))
                                    kilometrajes[p]=km
                                    break
                                except:
                                    print("Kms. es numérico!!")  
                        print("Modificado con EXITO!!!")   
                    else:
                        print("Patente NO existe!!")
                    break
                else:
                    print("Formato patente NO válido!!")                 
        else:
            print("No hay vehículos registrados!!")            
    elif(opcion==4):  
        while True: 
            patente=input("Ingrese patente => ")
            if(len(patente)==6):
                if(len(patentes)!=0):
                    existe=False
                    for p in range(len(patentes)):
                        if(patente==patentes[p]):
                            existe=True
                            pos=p
                            break
                    if existe:
                        propietarios.pop(p)
                        ruts.pop(p)
                        fonos.pop(p)
                        correos.pop(p)
                        patentes.pop(p)
                        annios.pop(p)
                        combustibles.pop(p)
                        puertas.pop(p)
                        transmisiones.pop(p)
                        colores.pop(p)
                        kilometrajes.pop(p)
                        preciosventas.pop(p) 
                        print("Vendido con EXITO!!!")   
                    else:
                        print("Patente NO existe!!")
                else:
                    print("No hay vehículos registrados!!")
                break
            else:
                print("Formato patente NO válido!!")  