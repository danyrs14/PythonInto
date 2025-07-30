#estructura de datos listas
frutas = ["manzana", "banana", "naranja", "fresa", "mango"]#creacion de la lista

#acceder a los elementos de la lista
print(frutas[0])#el cero entre corchetes indica el primero de la lista
print(frutas[1])#y asi sucesivamente como en este ejemplo
print(frutas[2])
print(frutas[3])
print(frutas[4])

#tambien se pueden acceder de esta manera
print(frutas[-1])#el -1 imprime el ultimo valor de la lista
print(frutas[-2])#y asi sucesivamente
print(frutas[-3])
print(frutas[-4])
print(frutas[-5])

#metodos de listas
frutas.append("pera")#metodo para agregar un elemento a la lista
print(frutas)

frutas.insert(1, "sandia")#metodo para agregar un elemento y indicar su pocision en la lista
print(frutas)

frutas.remove("banana")#metodo para eliminar elementos de una lista
print(frutas)

fruta_eliminada = frutas.pop(2)#elimina un elemento de la lista
print(frutas)#imprime la lista despues de la eliminacion
print(fruta_eliminada)#imprime el elemento eliminado

frutas.sort()#ordena los elementos de la lista en orden ascendente
print(frutas)

frutas.reverse()#ordena los elementos de la lista en forma descendente
print(frutas)

