#Crea una función que reciba cualquier cantidad de números y devuelva el promedio.

def promedio (*x):
    suma = sum(x)
    cantidad = len(x)
    prome = suma/cantidad
    return prome

print(promedio(10,23,5,6,7))