#Crea un conjunto con animales y verifica si un animal ingresado por el usuario está en él.

animales = {"Perro", "Gato", "Raton", "Murcielago"}

animal = str(input("Ingresa un animal: "))

if animal in animales:
    print("El animal:", animal, "efectivamente existe")
else:
    print("El animal:", animal, "no existe")