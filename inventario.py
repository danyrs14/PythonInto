#Crea un diccionario con productos y cantidades.
#Pide un producto y resta 1 a su cantidad si existe.
#Muestra el inventario actualizado.

inventario = {"Donas":5, "Cafe":15, "Agua":100, "Sandwich":13}

producto = str(input("Ingrese su producto: "))

if producto in inventario.keys():
    inventario[producto] = inventario[producto] - 1
else:
    print("No existe el producto:",producto)

print(inventario)