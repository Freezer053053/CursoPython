print("Introduce números, el programa finalizará cuando introduzcas un número menor al introducido anteriormente")

numero=int(input("Introduce números: "))
temp=0

numeros=[numero]

while temp<numero:
    print(str(numero))
    temp=numero
    numero=int(input("Introduce más números: "))
    if temp<numero:
        numeros.append(numero)

print("Los números introducidos son: " + str(numeros))
print("Programa finalizado")