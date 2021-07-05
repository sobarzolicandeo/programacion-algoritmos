# Enunciado 8
# Diego Sobarzo Licandeo
# PGY1121_004V

igual, aux = 0, 0
texto = input("Ingrese una palabra: ")
cantidadLetras = sum(c != ' ' for c in texto)
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print(f"¡Es palindromo y contiene {cantidadLetras} letras!")
else:
  print(f"!NO es palindromo y contiene {cantidadLetras} letras!")