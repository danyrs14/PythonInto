def funcion():
    # Código que puede generar una excepción personalizada
    if 5 > 10:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")