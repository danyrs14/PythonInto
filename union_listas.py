# Une dos listas (una de claves y otra de valores) en un diccionario.

claves = ["Nombre", "Apellido", "Edad"]

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))

valores = [nombre, apellido, edad]

info = {claves[0]:nombre, claves[1]:apellido, claves[2]:edad}

print(info)