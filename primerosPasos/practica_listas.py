miLista=["Pepe", "Juan", "Maria", "Alfredo"]

print(miLista[:]) # imprime la lista completa
print(miLista[2]) # imprime el dato en el indice 2
print(miLista[-1]) # imprime invitiendo el indice pero no empieza en 0
print(miLista[0:3]) # imprime desde el indice 0 incuido hasta el indice 2, el 3 esta excluido
print(miLista[:2]) # al no expecificar añade el indice 0
print(miLista[1:]) # accede a los elementos desde el indice 1 hasta el final

miLista.append("Alberto") # añade el elemento a la lista
miLista.insert(2, "Marta") # añade el elemento al indice 2
miLista.extend(["Ana", "Marcos", "Alex"]) # extiende la lista añadiendo los elementos

print(miLista[:])
print(miLista.index("Alfredo")) # imprime el indice del elemento Alfredo

miLista.remove("Ana") # elimina el elemento ana

miLista.pop() # elimina el ultimo elemento de la lista

print("Pepe" in miLista) # retorna true o false si el elemento se encuentra en la lista

miLista2=["Gabriel", "Jorge"]

miLista3=miLista+miLista2 # concatena las dos listas

print(miLista3[:])

miLista4=["Juan", "Maria"] * 3 #multiplica la lista 3 veces

print(miLista4[:])