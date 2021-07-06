# Enunciado 1
# Diego Sobarzo Licandeo
# PGY1121_004V

# Importar librerías necesarias
import numpy as np

# Funciones
def valorAsiento(a):
    asientos = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
    if a in asientos:
        return 78900 
    else:
        return 240000

# Definición de listas
opcion=0
nombresPasajeros=[]
rutsPasajeros=[]
telefonosPasajeros=[]
bancosPasajeros=[]
numerosAsientos=[]

# Definición de arreglos
a = np.reshape(np.array(range(1, 43)), (7, 6))
asientos = a.astype(str)

# Opciones del menú
while opcion!=5:
    opcion=0
    print("\n\t\tVuelos Duoc")
    print("="*46)
    print("1) Ver asientos disponibles")
    print("2) Comprar asiento")
    print("3) Anular vuelo")
    print("4) Modificar datos pasajeros")
    print("5) Salir")
    while opcion<1 or opcion>5:
        try:
            opcion=int(input("Ingrese opción => "))
            if opcion<1 or opcion>5:
                print("¡La opción ingresada no es válida!")
        except:
            print("¡La opción ingresada debe ser numérica!")
    # Ver asientos disponibles
    if(opcion==1):
        while True:
            try:
                print("\nAsientos disponibles:")
                asientosPrint = np.array2string(asientos, separator='  ', formatter={'str_kind': lambda asientos: asientos})
                print(' ' + asientosPrint[1:-1])
                break
            except:
                print("Error al obtener los asientos del vuelo")
    # Comprar asiento
    elif(opcion==2):
        # Seleccionar asiento
        while True:
            try:
                print("\nAsientos del vuelo:")
                asientosPrint = np.array2string(asientos, separator='  ', formatter={'str_kind': lambda asientos: asientos})
                print(' ' + asientosPrint[1:-1])
                numero=input('\nIngrese un número de asiento a reservar: ')
                if numero in asientos:
                    valor = valorAsiento(numero)
                    confirmacion=int(input(f"El asiento deseado tiene un valor de $ {valor}. ¿Confirma el asiento? [1: Si/ 2:No] => "))
                    if(confirmacion==1):
                        # Nombre pasajero
                        nombrePasajero=input("Ingrese Nombre y Apellido de pasajero => ")
                        nombresPasajeros.append(nombrePasajero)
                        # Rut Pasajero
                        rutPasajero=input("Ingrese rut de pasajero (Ej: 11222333-1) => ")
                        rutsPasajeros.append(rutPasajero)
                        # Télefono pasajero
                        telefonoPasajero=input("Ingrese teléfono de pasajero (Ej: 123456789) => ")
                        telefonosPasajeros.append(telefonoPasajero)
                        # Banco pasajero
                        bancoPasajero=int(input("Ingrese banco del pasajero [1: Banco Duoc/ 2:Otros] => "))
                        if(bancoPasajero==1):
                            bancosPasajeros.append("Banco Duoc")
                        elif(bancoPasajero==2):
                            bancoPasajero=input("Ingrese el nombre del banco => ")
                            bancosPasajeros.append(bancoPasajero)
                        else:
                            print("¡Banco debe ser 1 o 2!")
                            break
                        print("¡Se ha reservado el número de asiento {} exitosamente!".format(numero))
                        numerosAsientos.append(numero)
                        np.place(asientos, asientos == numero, 'X')
                        break
                    elif(confirmacion==2):
                        break
                    else:
                        print("¡La opción debe ser 1(Si) o 2(No)!")
                        break
                else:
                    print('El número de asiento {} NO se encuentra disponible'.format(numero))
            except:
                print("Error al seleccionar asiento")
    # Anular vuelo
    elif(opcion==3):
        while True: 
            numeroAsiento=input("Ingrese numero del asiento para anular el pasaje => ")
            if(len(numeroAsiento)!=0):
                if(len(numerosAsientos)!=0):
                    existe=False
                    for p in range(len(numerosAsientos)):
                        if(numeroAsiento==numerosAsientos[p]):
                            existe=True
                            pos=p
                            break
                    if existe:
                        np.place(asientos, asientos == 'X', numeroAsiento)
                        nombresPasajeros.pop(p)
                        rutsPasajeros.pop(p)
                        telefonosPasajeros.pop(p)
                        bancosPasajeros.pop(p)
                        numerosAsientos.pop(p)
                        print("¡Anulado exitosamente!")   
                    else:
                        print("¡Número de asiento no encontrado!")
                else:
                    print("¡Número de asiento no encontrado!")
                break
            else:
                print("¡Número de asiento no encontrado!")  
    # Modificar datos pasajeros
    elif(opcion==4):
        while True: 
            rutPasajero=input("Ingrese el rut del pasajero que desea editar => ")
            if(len(rutPasajero)!=0):
                if(len(rutsPasajeros)!=0):
                    existe=False
                    for p in range(len(rutsPasajeros)):
                        if(rutPasajero==rutsPasajeros[p]):
                            existe=True
                            pos=p
                            break
                    if existe:
                        print(f"{nombresPasajeros[p]} | {rutsPasajeros[p]} | {telefonosPasajeros[p]} | {bancosPasajeros[p]} | {numerosAsientos[p]}")
                        editar=int(input("¿Que dato desa editar? [1: Nombre/ 2:Teléfono] => "))
                        if(editar==1):
                            # Nombre pasajero
                            nombrePasajero=input("Ingrese Nombre y Apellido de pasajero => ")
                            nombresPasajeros[p] = nombrePasajero
                            print("¡Nombre editado exitosamente!")
                            break
                        elif(editar==2):
                            telefonoPasajero=input("Ingrese teléfono de pasajero (Ej: 123456789) => ")
                            telefonosPasajeros[p] = telefonoPasajero
                            print("¡Télefono editado exitosamente!")
                            break
                        else:
                            print("¡Experiencia debe ser 1, 2 o 3!")           
                    else:
                        print("¡Rut pasajero no encontrado!")
                else:
                    print("¡Rut pasajero no encontrado!")
                break
            else:
                print("¡Rut pasajero no encontrado!")