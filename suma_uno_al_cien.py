#Usa un for para sumar todos los números del 1 al 100 y muestra el resultado.
print("Suma de todos los numeros del 1 al 100")
suma = 0
for t in range(1,101):#itera del 1-100
    suma = suma + t

print(suma)#se imprime el resultado fuera del bucle ya que si lo ponemos dentro se imprimirian todos los resultados de cada iteracion y no el final