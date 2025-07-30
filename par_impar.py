#Usa for y continue para imprimir solo los números impares entre 1 y 20.
print("Numeros pares e impares del 1 al 20")

for n in range(1,21):#itera del 1 al 20
    if n % 2 == 0:#determinamos si es numero par
        continue#al ser pares descartamos el demas proceso y solo se imprimen los impares
    print(n)