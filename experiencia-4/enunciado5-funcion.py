# Enunciado 4
# Diego Sobarzo Licandeo
# PGY1121_004V

def funcion():
    primerNumero = float(input("Introduce un primer número: "))
    segundoNumero = float(input("Introduce un segundo número: "))
    if primerNumero > segundoNumero:
        return 1
    elif primerNumero < segundoNumero:
        return -1
    else:
        return 0
programa = funcion()
print(f"Valor devuelto: {programa}")