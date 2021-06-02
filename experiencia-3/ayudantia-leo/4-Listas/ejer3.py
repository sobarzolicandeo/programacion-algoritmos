'''
3)	Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower() y upper() ) .
Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.

'''
resp=""
lstNombres=[]
while resp.upper()!="NO":
    lstNombres.append(input("Ingrese un nombre: "))
    resp=input("Desea ingresar otro nombre? (si, no): ")
print(lstNombres)
pos=0
corto=len(lstNombres[0])
for i in range(len(lstNombres)):
    if(corto>len(lstNombres[i])):
        pos=i
        corto=len(lstNombres[i])

lstNombres.pop(pos)
print(lstNombres)