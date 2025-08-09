import random
import datetime

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

numero_aleatorio = random.randint(a,b)
print(numero_aleatorio)

fecha_actual = datetime.date.today()
print(fecha_actual)