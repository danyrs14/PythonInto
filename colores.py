# Crea dos conjuntos de colores. Muestra la unión y la intersección de ambos.

colores_primarios = {"Amarillo", "Rojo", "Azul", "Blanco"}

escala_de_grises = {"Gris", "Negro", "Blanco"}

union = colores_primarios | escala_de_grises
print(union)

intersection = colores_primarios & escala_de_grises
print(intersection)