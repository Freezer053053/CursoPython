contraseña=input("Introduce una contraseña: ")

for i in [range(2)]:
    if len(contraseña)<8:
        print("Contraseña demasiado corta")
        i=0
        contraseña=input("Introduce una contraseña: ")
    for j in contraseña:
        if j==' ':
            print("La contraseña no puede contener espacios en blanco")
            i=0
            contraseña=input("Introduce una contraseña: ")

entrada=input("Introduce la contraseña: ")

for i in range(1):
    if entrada==contraseña:
        print("Contraseña correcta")
        i=2
    else:
        for j in range(2):
            print("Contraseña incorrecta")
            j=0
            entrada=input("Introduce la contraseña: ")