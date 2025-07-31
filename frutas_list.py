#Crea una lista con 5 frutas.
#Agrega una fruta nueva, elimina la primera y muestra la lista final.

frutas = ["platano", "mango", "guayaba", "fresa", "piña"]

print("Frutas iniciales: ",frutas)

frutas.append("sandia")
print("Frutas post append: ",frutas)

frutas.remove("platano")
print("Frutas post remove: ",frutas)