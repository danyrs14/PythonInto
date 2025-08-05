#10/0 matematicamente esta mal y el programa pararia por ese error
#al ponerle una excepcion como esta esta hace que el programa no pare por ese error
#y simplemente sigue ejecutando el demas codigo
try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Error: Valor invalido")

#finally
try:
    archivo = open("main.txt", "r")
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    archivo.close()