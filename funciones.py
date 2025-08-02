#funciones
#llamada a una funcion
def saludo():
    print("Hola Mundo")

saludo()

#parametros y argumentos
#las funciones pueden aceptar parametros que son valores que se pasan a la funcion cuando se llama
def saludo2(nombre):
    print(f"Hola {nombre}")

#al llamar la funcion proporcionamos los argumentos correspondientes a los parametros
saludo2("Daniel")
saludo2("Luis")

#variables de retorno
#las variables pueden devolver valores utilizando la palabra return
def suma (a,b):
    return a+b

resultado = suma(3,4)
print(resultado)

#funciones anonimas o lambda
#son aquellas sin nombre definidas en una sola linea
cuadrado = lambda x: x ** 2
print(cuadrado(5))

#alcance de las varables global y local
def funcion():
    variable_local = 10
    print(variable_local)#accesible dentro de la funcion

varable_global = 20

def funcion2():
    print(varable_global)#accesible desde cualquier lugar

funcion()
funcion2()
print(varable_global)#esta no da error porque su alcance da para todos el codigo
#print(varable_local)#genera error porque su alcance solo es en la funcion

#funciones definidas por el usuario
def calcular_media(*x):#args (*) permite que la funcion acepte la cantidad que sea de elementos
    adicion = sum(x)#suma los elementos iterables
    cantidad = len(x)#devuleve la cantidad de elementos
    media = adicion / cantidad
    return media

print("La media: ", calcular_media(1,2,3,4,5,6))

#con lambda
more = lambda x: x + 2

print(more(5))

#documentacion de funciones
def area_rectangulo(base, altura):
    """
    Calcula el area del rectangulo.
    Args:
        base (float): base del rectangulo
        altura (float): altura del rectangulo

    Returns:
        float: area del rectangulo
    """
    return base * altura

print(area_rectangulo(2,3))

#funciones con numero variable de argumentos
def suma_variable(*numeros):#acetara el numero de elementos que sean
    total = 0#inicializa una variable en cero para irle agregando cantidades poco a poco
    for numero in numeros:#verifica si numero esta en numeros
        total = total + numero#de lo que va sumando lo va sumadno a su valor
    return total

print(suma_variable(1,2,3,4,5,6))
print(suma_variable(7,8,9,10,11,12))