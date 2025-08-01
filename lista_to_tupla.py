#Convierte una lista de colores en una tupla y muestra el resultado.
colores = ["Verde", "Azul", "Rojo", "Amarillo", "Naranja"]

print(colores)

colores_tupla = (colores[0], colores[1], colores[2], colores[3], colores[4])
colores_tupla2 = tuple(colores)
print("Tupla manual: ",colores_tupla)
print("Tupla automatica: ",colores_tupla2)
