# Enunciado 4
# Diego Sobarzo Licandeo
# PGY1121_004V

# Importar librería para trabajar promedios en arreglos
from numpy.lib.function_base import average

# Introducir números positivos entre 3 y 6 los cuales serán las dimensiones del arreglo bidimensional
# Filas
while True:
            try:
                fila=int(input("Ingresar número de filas => "))
                if(3<=fila<=6):
                    filas=fila
                    break
                else:
                    print("¡Valor para fila fuera de rango [3 - 6]!")
            except:
                print("¡El valor ingresado debe ser numérico!")
# Columnas
while True:
            try:
                columna=int(input("Ingresar número de columnas => "))
                print()
                if(3<=columna<=6):
                    columnas=columna
                    break
                else:
                    print("¡Valor para columna fuera de rango [3 - 6]!")
            except:
                print("¡El valor ingresado debe ser numérico!")

# Poblar la matriz con números reales
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input("Ingresar valor para fila {}, columna {} : ". format(i+1, j+1)))
        matriz[i].append(valor)

# Sumar las filas de la matriz
sumaFila=[sum(i) for i in matriz]
print (f"\nSuma por fila: {sumaFila}")

# Obtener el promedio de las columnas
promedioColumna=[average(i) for i in zip(*matriz)]
print (f"\nPromedio por columna: {promedioColumna}")

# Imprimir los valores del arreglo
print("\nValores del arreglo bidimensional:")
for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print ("{}".format(elemento), end= " ")
    print("]")
print()