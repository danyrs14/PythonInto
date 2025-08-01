#Crea un diccionario con nombres como claves y teléfonos como valores.
#Pide al usuario un nombre y muestra su teléfono si existe.

clientes = {"Daniel":"5512345678", "Luis":"5509876543", "Ernesto":"5523456789"}

print(clientes["Daniel"])

nombre = str(input("Ingrese su nombre: "))

if nombre in clientes.keys():#se usa in para ver si existe entre las claves
    #si se usara == mandaria error porque no estaria comparando a todos los valores
    print("El nombre", nombre, "su telefono es:", clientes[nombre])
else:
    print("El nombre", nombre, "no existe")
