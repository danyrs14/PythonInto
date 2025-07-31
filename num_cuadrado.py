#Crea una lista de números del 1 al 10.
#Crea una segunda lista que contenga cada número al cuadrado usando un for.

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

numeros_cuadrados = [x**2 for x in numeros]#multiplica el contador al cuadrado y itera en los numeros de la lista
print(numeros_cuadrados)