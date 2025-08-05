"""
Pida al usuario el nombre de un archivo a abrir.
Intente abrirlo en modo lectura ("r").
Si el archivo no existe, captura el error y muestra: "El archivo no fue encontrado."
Si se abre correctamente, imprime su contenido.
Usa finally para cerrar el archivo si fue abierto exitosamente.
"""
try:
    archivo1 = str(input("Ingresa el nombre de un archivo a abrir: "))
    # Abrir y leer un archivo
    with open(archivo1, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
