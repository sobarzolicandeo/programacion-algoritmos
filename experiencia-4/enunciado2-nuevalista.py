primeralista=[1, 5, 7, 'a', 'b']
segundalista=['a', 'b']

repetidos = []
for i in primeralista:
    if i in segundalista:
        repetidos += [i]
print(f"Palabras que aparecen en las dos listas: {repetidos}")