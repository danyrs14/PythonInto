#Pide al usuario un número y verifica si está en una lista.
#Muestra un mensaje indicando si lo encontró o no.

numeros = [13,26,37,43,59,61,76,84,90,103]

num = int(input("Digite um numero: "))

for x in numeros:
    if x == num:
        print("El numero",num,"esta en la lista")
    else:
        print("El numero",num,"no esta en la lista")
        break
