#Crea una función que acepte un número variable de nombres y los imprima uno por uno.

n = int(input("Ingresa un numero: "))#numero variable de nombres
m = 0#pivote

lista = []#creamos lista vacia

for x in range(n):
    if x == m:
        lista.append(str(input("Ingresa un Nombre: ")))#cada iteracion le agregamos un elemento a la lista
        m = m + 1
    else:
        break

#a medias