# Enunciado 7
# Diego Sobarzo Licandeo
# PGY1121_004V

# Función que recoje los números de la secuencia y como segundo argumento un núermo entero entre 10 y 15
def fibonachi(n,numero):
    secuencia=[]
    a, b = 0,1
    while a < n:
        a, b = b, a+b
        secuencia.append(a)
    print(secuencia[0:numero])
 
numero=int(input("Ingrese un numero entre 10 y 15: "))
while numero<10 or numero>15:
    print("El número ingresado debe estar comprendido entre 10 y 15")
    numero=int(input("Ingrese un numero entre 10 y 15: "))
secuencia=fibonachi(1000,numero)