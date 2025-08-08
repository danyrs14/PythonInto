"""
Crea una función llamada validar_edad() que:
Reciba un parámetro edad.
Si la edad es menor que 18, lance una excepción personalizada con el mensaje "Edad inválida. Debes ser mayor de 18 años.".
Si la edad es mayor o igual a 18, la función debe retornar "Edad válida.".
Luego, en el bloque try, llama a la función validar_edad(), pasando una edad proporcionada por el usuario, y maneja el error con una excepción que imprima el mensaje de error adecuado.
"""

a = int(input("Ingresa tu edad: "))

def validar_edad(edad):
    if edad < 18:
        raise Exception("Edad invalidada, debe ser mayor de 18.")
    else:
        return print("Edad validada")

try:
    validar_edad(a)
except Exception as e:
    print(f"Error: {str(e)}")