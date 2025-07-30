#Pide números al usuario en un while y acumúlalos.
#El bucle termina cuando ingresa 0.
print("Ingresa numeros y cuando ingreses el cero terminara todo")

contador = 0#inicializamos el ciclo en cero
while True:#ponemos un true para que el ciclo sea indefinido
    contador += 1#lo vamos aumentando de uno en uno
    numero = int(input("Ingrese numero: "))#para que el ususario ingrese numeros conforme avanza el ciclo

    if numero == 0:#cuando el ususario ingrese el cero
        break#el ciclo terminara

#nota: to do se hace dentro del ciclo para que el ususario vaya ingresando los datos las veces que sean hasta que ingrese cero
