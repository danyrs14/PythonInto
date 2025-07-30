#tuplas
#creacion y acceso
punto = (3,4)#tupla
#para acceder
print(punto[0])
print(punto[1])
#nota aunque es similar a las listas la diferencia es que los datos de la tupla son inmutables

#metodos de tuplas
mi_tupla = (1,2,3,4,2,4,2)

print(mi_tupla.index(2))#devuelve el indice de la primera aparicion de un elemento de una tupla
print(mi_tupla.index(2,2))#value es el elemento y start es la cantidad en la que aparece
#en este caso es el valor 2 y el start indica la segunda ves que aparece
#si ponemos un 1 de valor y le ponemos la segunda vez marcara error
