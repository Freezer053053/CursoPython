import re  # Importa el módulo de expresiones regulares

# Define una lista de nombres
lista_nombres = [
    "Ana Gómez",
    "María Martín",
    "Sandra López",
    "Santiago Martín",
    "Sandra Fernández"
]

# Itera sobre cada elemento en la lista de nombres
for elemento in lista_nombres:
    # Busca nombres que comiencen con "Sandra"
    if re.findall("^Sandra", elemento):
        print(elemento)  # Imprime el nombre si comienza con "Sandra"

# Itera nuevamente sobre cada elemento en la lista de nombres
for elemento in lista_nombres:
    # Busca nombres que terminen con "Martín"
    if re.findall("Martín$", elemento):
        print(elemento)  # Imprime el nombre si termina con "Martín"