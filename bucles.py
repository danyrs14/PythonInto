#bulce for
print("Numeros del 1 al 5 multiplicados por 2 con bucle for:")
for numero in range(1, 6):#itera del 1-5
    print(numero*2)#al final multiplica numero * 2 al llegar al menor que 6

#bucle while
print("Numeros del 1 al 5 con bucle while:")
contador = 1#inicializamos
while contador <= 5:#mientras llegue a un numero menor igual a 5
    print(contador*2)#contador ira multiplicando * 2
    contador += 1#y su incremento sera de uno en uno

#control de bucles (break)
print("Control de Bucle con break")
contador = 0
while True:#el bucle while se ejucta indefinidamente por el true
    print(contador)
    contador += 1

    if contador == 5:#para controlar el bucle ponemos una condicional para cuando llegue exactamente a 5
        break#se termina el ciclo con break

#control de bucles (continue)
print("Control de Bucle con continue")
for i in range(10):#itera sobre el 0-9
    if i % 2 == 0:#se verifica si es un numero par
        continue#si es par se ejecuta continue
    print(i)#lo que hace que ignore a los numero pares al saltarse el resto del codigo en este caso el print(i)
    #por eso solo salen los numero impares al compilarlo

#control de bucles (pass)
print("Control de Bucle con pass")
for i in range(5):#itera sobre 0-4
    pass#la instruccion pass es nula se usa para no realizar ninguna accion
#su uso se basa en dejar funciones hechas para implementarlas mas tarde