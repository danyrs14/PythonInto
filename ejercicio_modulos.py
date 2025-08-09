"""
Importe los módulos math, random y datetime.
Usa math para calcular la raíz cuadrada de un número que el usuario ingrese.
Usa random para generar un número aleatorio entre 1 y 100.
Usa datetime para mostrar la fecha y hora actual.
Imprime todos esto en pantalla.
"""

import math
import random
import datetime

a = int(input("Ingresa un numero: "))

resultado = math.sqrt(a)
print(resultado)

b = int(input("Ingresa un numero: "))
c = int(input("Ingresa un numero: "))

aleatorio = random.randint(b, c)
print(aleatorio)

fecha_actual = datetime.date.today()
print(fecha_actual)

