# Se ejecutará el ciclo While hasta que NO se cumpla la condicion
# en este caso, la condicion es que opc sea distinta a 0
# se saldrá cuando, opc sea igual a 0
opc=1
while opc!=0:
    opc=int(input("Menu\n\t1. Opcion\n\t2. Pocion\n\t0. Salir\nIngrese su opción: "))
    # Si la opcion es 1 o 2, mostrara la "opcion elegida"
    if opc==1 or opc==2:
        print(f"\nOpcion elegida: {opc}\n")
        # Si no, si es distinta a 0, mostrara el mensaje de "Opcion no valida"
    elif opc!=0:
        print("Opcion no valida")
print("Terminó el While")