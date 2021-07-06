# Enunciado 6
# Diego Sobarzo Licandeo
# PGY1121_004V

# Importar librerías necesarias
import math

# Importar Funciones
from experiencia4Funciones import *

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



