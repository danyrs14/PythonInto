#Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10 usando for.
print("Tabla de multiplicar")
numero = int(input("Ingresa un numero del 1 al 10: "))#se usa input para pedirle al usuario que ingrese
print("Tabla del", numero)
for t in range(1,11):#iterar del 1-10
    print(t*numero)