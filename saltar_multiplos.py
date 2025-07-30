#imprime los números del 1 al 20 usando for, pero usa continue para saltar los múltiplos de 3.
print("Prohibidos los multiplos de 3")
for multiplos in range(1,21):#rango del 1 al 20
    if multiplos % 3 == 0:#determinamos los multiplos de 3
        continue # si si lo son entonces el proceso posterior lo ignora y descarta a esos numeros
    print(multiplos)