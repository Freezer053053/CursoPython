midiccionario={"Alemania":"Berlin", "España":"Madrid"}
midiccionario["Italia"]="Lisboa" #agregamos al diccionario
print(midiccionario)
midiccionario["Italia"]="Roma"  #lo reemplazamos
print(midiccionario)
del midiccionario["España"] # elimina el elemento   
print(midiccionario)
#-----------------------------------------------------------------
mitupla=["España", "Francia", "Italia"]
minuevodiccionario={mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Roma"} #asignamos las tuplas como claves
#-----------------------------------------------------------------
otronuevodiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993.1996,1997,1998]} #multiples valores para una clave
print(otronuevodiccionario["anillos"]) #accedo a la asignacion de la clave
#-----------------------------------------------------------------
otronuevodiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993.1996,1997,1998]}} #diccionario dentro de otro
print(otronuevodiccionario["anillos"]) #accedo a la asignacion de la clave
#-----------------------------------------------------------------
print(midiccionario.keys()) #imprime las claves del diccionario
print(midiccionario.values()) #imprime los valeres de las claves del diccionario
print(len(midiccionario)) #imprime la longitud del diccionario