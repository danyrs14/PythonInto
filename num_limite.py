#Usa un while True que pida números al usuario.
#Si ingresa un número negativo, termina el bucle con break.
contador = 0#inicializamos en cero el ciclo
while True:#bucle indefinido
    contador += 1#incrementa de uno en uno
    numero = int(input("Ingresa un numero: "))#cada incremento el ususario va ingresando un numero

    if numero == -1:#si el numero es -1 el ciclo se termina
        break#gracias al break

#nota: al ser un while True el bucle no terminara a menos que le pongamos un break