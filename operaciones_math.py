#Crea una función que reciba dos números y devuelva:
#Suma
#Resta
#Multiplicación
#Imprime los resultados.

x = int(input("Ingrese un numero: "))#pedimos numero x
y = int(input("Ingrese otro numero: "))#pedimos numero y

operacion = str(input("Ingrese operacion: A = Suma, B = Resta, C = Multiplicacion, D = Division\n"))

def mate(a, b):#creamos los parametros
    if operacion == "A":
        return a + b
    elif operacion == "B":
        return a - b
    elif operacion == "C":
        return a * b
    elif operacion == "D":
        return a / b
    else:
        print("Operacion no valida")


resultado = mate(x,y)#mandamos llamar a la funcion asignando los valores agregados por el ususario como paramentros
print(resultado)