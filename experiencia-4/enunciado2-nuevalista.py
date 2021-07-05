#Dadas dos listas pobladas con elementos de tipo carácter, 
# se pide generar una tercera sólo con los elementos que estén repetidos en ellas. 
# Considerar que la nueva lista no contenga elementos duplicados.

primeralista=[1, 5, 7, 'a', 'b']
segundalista=['a', 'b', 'b']

for i in range(len(primeralista) - 1, -1, -1):
              if primeralista[i] in primeralista[:i]:
                  del primeralista[i]

for i in range(len(segundalista) - 1, -1, -1):
              if segundalista[i] in segundalista[:i]:
                  del segundalista[i]

repetidos = []
for i in primeralista:
    if i in segundalista:
        repetidos += [i]
print(f"Palabras repetidas en las listas: {repetidos}")