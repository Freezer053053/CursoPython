miTupla=("Álex", 23, 10, 2005) #declaramos una tupla

miLista=list(miTupla) #miTupla ahora es una liSta en miLista

miTupla2=tuple(miLista) #Transformamos la lista a una tupla

print(miTupla.count(3)) # me indica cuantas veces aparece el elemento
print(len(miTupla)) #indica la cantidad de elementos

miTupla3=("Juan",)  #tupla unitaria

nombre, dia, mes, agno = miTupla #almacena los valores de la tupla
print(nombre)
print(dia)
print(mes)
print(agno)