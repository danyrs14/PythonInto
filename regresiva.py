#Muestra los números del 10 al 1 usando while.
print("Cuenta regresiva del 10 al 1")
contador = 10#inicializamos en 10 para empezar el decremento desde ahi
while contador >= 0:#le ponemos un limite al ciclo que sea mayor igual a cero
    print(contador)#lo vamos imprimiendo
    contador -= 1#decrece uno cada ves
    if contador == 0:#hasta que llegue a cero lo paramos
        break#sino paramos se descontrola

#nota: hay que tener cuidado con el while ya que si no se usa bien el resultado podria ser infinitpo