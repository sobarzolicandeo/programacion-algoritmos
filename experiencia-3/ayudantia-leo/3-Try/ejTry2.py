# Validar que dos numeros sean enteros
# while True:
#     try:
#         num1=int(input("Ingrese el 1er número: "))
#         num2=int(input("Ingrese el 2do número: "))
#         break
#     except:
#         print("Valor debe ser numérico")

# Dividir dos enteros y pedir si desea continuar
# continuar=True
# while continuar:
#     while True:
#         try:
#             num1=int(input("Ingrese el 1er número: "))
#             num2=int(input("Ingrese el 2do número: "))
#             break
#         except:
#             print("Valor debe ser numérico")
#     r=round(num1/num2)
#     print(f"{num1}/{num2}={r}")
#     resp=input("Desea realizar un nuevo calculo? (n:NO): ")
#     if resp.upper()=="N": # if resp.lower()=="n"
#         continuar=False
# print("Saliendo del sistema")

#################
# Version mejorada mismo caso anterior.
# Se incluye validacion al dividir por 0 y se cambia respuesta de nuevo calculo por numero para incluir otra validacion
continuar=True
while continuar:
    while True:
        try:
            num1=int(input("Ingrese el 1er número: "))
            num2=int(input("Ingrese el 2do número: "))
            r=num1/num2
            break
        except ZeroDivisionError:
            print("El 2do número no puede ser Cero")
        except:
            print("Valor debe ser numérico")
    print(f"{num1}/{num2}={r}")
    while True:
        try:
            resp=int(input("Desea realizar un nuevo calculo? (0:NO): "))
            break
        except:
            print("Ingrese valor numérico")
    if resp==0:
        continuar=False
print("Saliendo del sistema")