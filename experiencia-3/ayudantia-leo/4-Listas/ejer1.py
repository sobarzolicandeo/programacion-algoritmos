'''
1)	Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla.
'''
nombres=[]
cont=0
# solicito 3 nombres y los guardo en mi lista
while cont<3:
    nombres.append(input("Ingrese un nombre: "))
    cont+=1
# mostrar lista
print(nombres)
# recorrer la lista, buscar el nombre mas largo y lo muestro
largo=0
for i in range(3):
    if(largo<len(nombres[i])):
        pos=i
        largo=len(nombres[i])
print(f"El nombre con más caracteres es: {nombres[pos]}")