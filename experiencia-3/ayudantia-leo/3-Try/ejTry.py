# Ejemplo de ingresar la edad con Try
# try:
#     edad = int(input("Ingrese su edad: "))
#     print(f"La edad ingresada es: {edad}")
# except:
#     print("La edad debe ser número.")


# Ejemplo de ingresar la edad con Try dentro de un While
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except:
        print("La edad debe ser número.")
print(f"La edad ingresada es: {edad}")