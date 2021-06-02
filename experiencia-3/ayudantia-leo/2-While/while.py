#multiplicar por 6 un numero mayor a 30
# n=30
# while n<=30:
#     n=int(input("Ingrese un numero mayor a 30: "))
# print(f"{n}*6={n*6}")


#while con acumulador y flag
continuar=True
contador=1
while continuar:
    contador*=3 #contador = contador * 3
    print(contador)
    if contador>100:
        continuar=False
print(f"El ultimo valor del contador es de: {contador}")