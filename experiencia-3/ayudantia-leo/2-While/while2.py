# while inicializado en True y se sale con break
while True:
    n=int(input("Ingrese numero entre 100 y 200: "))
    if 100<=n<=200: # if n>=100 and n<=200
        break
    else:
        print("Fuera de Rango!!!")
if n%2==0:
    print(f"{n} es par")
else:
    print(f"{n} es impar")