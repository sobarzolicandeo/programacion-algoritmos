'''
Calcular la potencia de un numero usando ciclos (no podra usar el operador aritmetico **), para ellos, el sistema solicitará por pantalla el valor de la base y el valor del exponente (ejemplo, base=4, exponente=2, entonces el resultado será 16), una vez realizado el calculo se mostrara el resultado por una salida por pantalla mostrando la informacion de la siguiente manera:
"El resultado de la potencia de base 4 y exponente 2 es 16"
'''
# Las potencia es el numero base multiplicado por el exponente esa cantidad de veces por si mismo. 
# Por ejemplo base 3 exponente 4, es 3*3*3*3 lo que da 81

# Solicitamos los dos numeros y validamos
while True:
    try:
        base=int(input("Ingresar número base (Mayor a Cero): "))
        exponente=int(input("Ingresar número exponente (Mayor a Cero): "))
        if base>0 and exponente>0:
            break
    except:
        print("Ingrese solo números.")
# Realizamos el calculo de la potencia
potencia=1
for i in range(exponente):
    potencia*=base # potencia = potencia * base
print(f"El resultado de la potencia de base {base} y exponente {exponente} es {potencia}")