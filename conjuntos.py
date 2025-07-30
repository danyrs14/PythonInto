#conjuntos
#se pueden crear de las 2 maneras
paises = {"Mexico", "Argentina", "Brasil"}
print(paises)
numeros = set([1,2,3,4,5])
print(numeros)

conjunto1 = {1,2,3}
print("Conjunto 1: ",conjunto1)
conjunto2 = {3,4,5}
print("Conjunto 2: ",conjunto2)
#operaciones matematicas
union = conjunto1 | conjunto2#la union de 2 conjuntos solo imprime una ves los elementos comunes entre los conjuntos
print("Union: ",union)#tambien ordena en forma asendente los datos

intersection = conjunto1 & conjunto2#la interseccion imprime 1 ves el valor comun entre los 2 conjuntos
print("Interseccion: ",intersection)#en este caso imprime el 3

diferencia = conjunto1 - conjunto2#la diferencia funciona de la siguiente manera el valor de la izquierda quita los elementos que tenga en comun con el de la derecha e imprime
print("Diferencia: ",diferencia)

diferencia_simetrica = conjunto1 ^ conjunto2#la dif simetrica solo imprime los valores de ambos conjuntos y descarta los elementos en comun
print("Diferencia simetrica: ",diferencia_simetrica)

