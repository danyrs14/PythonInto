#diccionarios
#creacion y acceso
persona = {"nombre": "Daniel", "edad": "23", "ciudad": "CDMX"}#diccionario creado
print(persona["nombre"])#para imprimir datos basta con indicar la clave
print(persona["edad"])
print(persona["ciudad"])

#metodos diccionarios
print("Metodos")
print(persona.keys())#imprime las claves del dicionario
print(persona.values())#imprime los valores del diccionario
print(persona.items())#imprime una lista de los pares calve : valor

persona.update({"profesion": "ingeniero en sistemas"})#es para agregar un par clave valor al diccionario
print(persona)