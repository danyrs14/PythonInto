"""Pida al usuario dos números (dividendo y divisor).
Intente dividirlos.
Si el divisor es cero, captura el error y muestra un mensaje como: "No se puede dividir entre cero."
Si el usuario ingresa algo que no sea número, muestra: "Entrada inválida."
Usa finally para imprimir "Operación finalizada." pase lo que pase."""
try:
    a = int(input("Introduce un numero: "))
    b = int(input("Introduce otro numero: "))
except ValueError:
    print("Valor invalido")
finally:
    print("Calculando")

def dividir(x,y):
    return x/y

try:
    print(dividir(a,b))
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except NameError:
    print("No se pudo dividir nada")
finally:
    print("Finalizando")