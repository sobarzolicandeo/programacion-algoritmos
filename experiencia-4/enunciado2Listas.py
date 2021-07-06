# Enunciado 2
# Diego Sobarzo Licandeo
# PGY1121_004V

# Declaración de listas
primeralista=[1, 1, 2, 2, 'a', 'b']
segundalista=['a', 'a', 'b', 'b', 8, 0, 3, 5]

# Eliminar los valores duplicados de la primera lista
for i in range(len(primeralista) - 1, -1, -1):
              if primeralista[i] in primeralista[:i]:
                  del primeralista[i]

# Eliminar los valores duplicados de la segunda lista
for i in range(len(segundalista) - 1, -1, -1):
              if segundalista[i] in segundalista[:i]:
                  del segundalista[i]

# Lista con los elementos repetidos en las listas
repetidos = []
for i in primeralista:
    if i in segundalista:
        repetidos += [i]
print(f"Palabras repetidas en las listas: {repetidos}")