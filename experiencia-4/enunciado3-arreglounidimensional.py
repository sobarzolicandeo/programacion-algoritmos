# Enunciado 3
# Diego Sobarzo Licandeo
# PGY1121_004V

# Importar librerías para trabajar arreglos y random
import numpy as np
import random as rd

# Declarar y poblar un arreglo unidimensional de largo 10 con números enteros positivos
arreglo=np.array(10)
arreglo=[0]*10
for i in range(len(arreglo)):
    arreglo[i]=rd.randrange(10)
print("Valores del arreglo unidemensional:")
for i in range(len(arreglo)):
    print(arreglo[i], end=" ")

# Ingresa un número e indicar si se encuentra en el arreglo
numero=int(input('\n\nIngrese un número: '))
if numero in arreglo:
    print("El número {} se encuentra en el arreglo".format(numero))
else:
    print('El número {} NO se encuentra en el arreglo'.format(numero))








