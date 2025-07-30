#Crea un bucle while que pida al usuario adivinar un número secreto.
#Termina cuando acierte usando break.
print("Adivina el numero secreto")
numero = int(input("Ingresa un numero\n"))
contador = 0#inicializamos el bucle en cero
while True:#ponemos en true el while para que la cuenta sea indefinida
    contador += 1#incrementamos el contador de uno en uno

    if contador == numero:#comparamos los 2 numeros
        break#terminamos el ciclo cuando el contador y el numero ingresado coincidan

print("Numero secreto = ", contador, "Numero ingresado = ", numero)#imprimimos el resultado

