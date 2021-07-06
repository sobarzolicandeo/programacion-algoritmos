# Finciones
# Diego Sobarzo Licandeo
# PGY1121_004V

# Importar librerías necesarias
import math

# Enunciado 1
def valorAsiento(a):
    asientos = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
    if a in asientos:
        return 78900 
    else:
        return 240000

# Enunciado 6
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

# Enunciado 7
def fibonachi(n,numero):
    secuencia=[]
    a, b = 0,1
    while a < n:
        a, b = b, a+b
        secuencia.append(a)
    print(secuencia[0:numero])