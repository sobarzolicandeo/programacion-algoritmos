# Enunciado 6
# Diego Sobarzo Licandeo
# PGY1121_004V

# Importar librerías necesarias
import math

# Funciones
def areaCirculo():
    print("Ingrese el radio de círculo en cm: ")
    r = float(input())
    a = math.pi * (r*r)
    print("El área del círculo con radio",r, "es",a)

def perCuadrado():
    print("Ingrese la medida de un lado del cuadrado en cm: ")
    r = float(input())
    a = r*4
    print("El perímetro del cuadrado es",a)

# Opciones del menú
opcion=0
while opcion!=3:
    opcion=0
    print()
    print("\tSeleccione cálculo a realizar")
    print("="*44)
    print("1) Área de un círculo")
    print("2) Perímetro de un cuadrado")
    print("3) Salir")
    while opcion<1 or opcion>4:
        try:
            opcion=int(input("Ingrese opción => "))
            if opcion<1 or opcion>4:
                print("¡La opción ingresada no es válida!")
        except:
            print("¡La opción ingresada debe ser numérica!")
    if(opcion==1):
        areaCirculo()
    elif(opcion==2):
        perCuadrado()
    elif(opcion==3):
        exit()



