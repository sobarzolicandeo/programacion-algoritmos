# Enunciado 7
# Diego Sobarzo Licandeo
# PGY1121_004V

# Importar Funciones
from experiencia4Funciones import *
 
numero=int(input("Ingrese un numero entre 10 y 15: "))
while numero<10 or numero>15:
    print("El número ingresado debe estar comprendido entre 10 y 15")
    numero=int(input("Ingrese un numero entre 10 y 15: "))
secuencia=fibonachi(1000,numero)