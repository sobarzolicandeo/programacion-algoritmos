# Validar ingreso de dos numeros positivos y ofrecer las 4 opciones básicas
# Repetir hasta que el usuario quiera
# continuar=True
# while continuar:
#     n1=0
#     while n1<=0:
#         n1=int(input("Ingrese primer numero (mayor a cero) -> "))
#     n2=0
#     while n2<=0:
#         n2=int(input("Ingrese segundo numero (mayor a cero) -> "))
#     # Menu
#     print("\tMenu Calculadora")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     oper=int(input("Ingrese Opcion: "))
#     if 1<=oper<=4: # if oper>=1 and oper<=4
#         if oper==1:
#             print(f"{n1}+{n2}={n1+n2}")
#         elif oper==2:
#             print(f"{n1}-{n2}={n1-n2}")
#         elif oper==3:
#             print(f"{n1}*{n2}={n1*n2}")
#         else:
#             division=round(n1/n2)
#             print(f"{n1}/{n2}={division}")
#         resp=input("¿Desea continuar (n:NO)? -> ")
#         if resp.upper()=="N":
#             continuar=False
#     else:
#         print("Error opcion")
# print("Hasta pronto")


##############################
# Version Optimizada Profe
continuar=True
while continuar:
    n1=0
    while n1<=0:
        n1=int(input("Ingrese primer numero (mayor a cero) -> "))
    n2=0
    while n2<=0:
        n2=int(input("Ingrese segundo numero (mayor a cero) -> "))
    # Menu
    while True:
        print("\tMenu Calculadora")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        oper=int(input("Ingrese Opcion: "))
        if 1<=oper<=4:
            break
        else:
            print("Error opcion")
    if oper==1:
        print(f"{n1}+{n2}={n1+n2}")
    elif oper==2:
        print(f"{n1}-{n2}={n1-n2}")
    elif oper==3:
        print(f"{n1}*{n2}={n1*n2}")
    else:
        print(f"{n1}/{n2}={n1/n2}")
    resp=input("¿Desea continuar (n:NO)? -> ")
    if resp.upper()=="N":
        continuar=False
print("Hasta pronto")