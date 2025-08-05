#Crea una función que acepte un número variable de nombres y los imprima uno por uno.

def imprimir_nombres():
    n = int(input("Ingresa un número: "))  # número de nombres a ingresar
    m = 0  # pivote
    lista = []  # lista vacía

    for x in range(n):
        if x == m:
            lista.append(str(input("Ingresa un Nombre: ")))  # agregamos nombre
            m = m + 1
        else:
            break

    print("\nNombres ingresados:")
    for nombre in lista:
        print(nombre)

# Llamada a la función
imprimir_nombres()
