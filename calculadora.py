"""
Pide al usuario dos números.
Ofrece un menú con opciones: suma, resta, multiplicación y división.
Realiza la operación correspondiente y muestra el resultado.
Si el usuario elige dividir, maneja la excepción de dividir entre cero.
"""
import operaciones_aritmeticas

print("A = suma")
print("B = resta")
print("C = multiplicacion")
print("D = division")
operacion = str(input("Operacion: "))

if operacion == "A":
    a = int(input("Ingresa el valor: "))
    b = int(input("Ingresa el valor: "))
    operaciones_aritmeticas.sumar(a, b)
elif operacion == "B":
    a = int(input("Ingresa el valor: "))
    b = int(input("Ingresa el valor: "))
    operaciones_aritmeticas.resta(a, b)
elif operacion == "C":
    a = int(input("Ingresa el valor: "))
    b = int(input("Ingresa el valor: "))
    operaciones_aritmeticas.multiplicacion(a, b)
elif operacion == "D":
    a = int(input("Ingresa el valor: "))
    b = int(input("Ingresa el valor: "))
    try:
        operaciones_aritmeticas.division(a, b)
    except ZeroDivisionError:
        print("Division by zero")


