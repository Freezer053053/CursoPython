print("introduzca números positivos, introduce cualquier número negativo para finalizar")

numero=int(input("Introduzca números: "))
numeros=[numero]
temp=numero

while numero>0:
    numero=int(input("Introduzca más números: "))
    if numero>0:
        temp=temp+numero
        numeros.append(numero)

print(temp)

