for i in ["Pepe", 3, 2, "Álex"]: # El bucle recorre una lista
    print("Hola", end=" ") #Hacemos que en vez de acabar el print con un salto de linea lo acabe con un espacio en blanco
    #print(i)
#---------------------------------------------------------
for i in "deborah.alexfs@gmail.com": # El bucle recorre un string
    print(i)
#---------------------------------------------------------
for i in range(5): #Crea como un array de 5 elementos empezando desde 0
    print(f"Valor de la variable {i}") # f para concatenar string y variables
#---------------------------------------------------------
for i in range(5, 10): #cuenta desde 5 hasta 9
    print(f"Valor de la variable {i}") # f para concatenar string y variables
#---------------------------------------------------------
for i in range(5, 50, 3): #cuenta desde 5 hasta 49 en intervalos de 3
    print(f"Valor de la variable {i}") # f para concatenar string y variables
#---------------------------------------------------------
valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):
    if i=='@':
        valido==True

if valido==True:
    print("Email correcto")
else:
    print("Email incorrecto")