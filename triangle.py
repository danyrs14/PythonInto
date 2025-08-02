#Define una función que calcule el área de un triángulo dado base y altura.
#Devuelve el resultado con return.

base = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))

def triangulo(a, b):
    return (a*b)*(0.5)

resultado = triangulo(base, altura)
print(resultado)