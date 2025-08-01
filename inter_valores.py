#Usa una tupla para intercambiar el valor de dos variables (ejemplo: a = 5, b = 10 → a = 10, b = 5).
a = int(input("Digite el numero a: "))
b = int(input("Digite el numero b: "))

a, b = b, a#el lado derecho python lo toma como una tupla implicita
#las de los ejemplos del curso son tuplas explicitas como esta valores = (a, b)

print("Valor a: ",a)
print("Valor b: ",b)