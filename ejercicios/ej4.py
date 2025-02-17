puntos=0
arrobas=0
email=input("Por favor introduce un email válido: ")

for i in email:
    if i=='.':
        puntos+=1
    if i=='@':
        arrobas+=1

if puntos>0 and arrobas==1:
    print("El email es correcto")
else:
    print("El email es incorrecto")