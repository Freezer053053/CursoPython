import re  # Importa el módulo de expresiones regulares

# Define una lista de nombres
lista_nombres = [
    "Ana",
    "María",
    "Sandra",
    "Santiago",
    "Sandra"
]

# Itera sobre cada elemento en la lista de nombres
for elemento in lista_nombres:
    # Busca nombres que contengan cualquier letra entre 'o' y 't'
    if re.findall("[o-t]", elemento):
        print(elemento)  # Imprime el nombre si contiene letras entre 'o' y 't'

# Itera nuevamente sobre cada elemento en la lista de nombres
for elemento in lista_nombres:
    # Busca nombres que comiencen con cualquier letra entre 'O' y 'T'
    if re.findall("^[O-T]", elemento):
        print(elemento)  # Imprime el nombre si comienza con letras entre 'O' y 'T'

# Itera nuevamente sobre cada elemento en la lista de nombres
for elemento in lista_nombres:
    # Busca nombres que terminen con cualquier letra entre 'o' y 't'
    if re.findall("[o-t]$", elemento):
        print(elemento)  # Imprime el nombre si termina con letras entre 'o' y 't'

# Define una lista de pedidos
lista_pedidos = [
    "Ma.1",
    "Se1",
    "Se2",
    "Ma.2",
    "Ba1",
    "Ma3",
    "Ma:A",
    "MaB",
    "Ma:C",
    "MaD"
]

# Itera sobre cada elemento en la lista de pedidos
for elemento in lista_pedidos:
    # Busca pedidos que comiencen con "Ma" seguido de un número entre 0 y 2 o una letra entre A y C
    if re.findall("Ma[0-2A-C]", elemento):
        print(elemento)  # Imprime el pedido si coincide con el patrón

# Itera nuevamente sobre cada elemento en la lista de pedidos
for elemento in lista_pedidos:
    # Busca pedidos que comiencen con "Ma" seguido de cualquier carácter que no sea un número entre 0 y 2
    if re.findall("Ma^[0-2]", elemento):
        print(elemento)  # Imprime el pedido si coincide con el patrón

# Itera nuevamente sobre cada elemento en la lista de pedidos
for elemento in lista_pedidos:
    # Busca pedidos que comiencen con "Ma" seguido de un punto (.) o dos puntos (:)
    if re.findall("Ma[.:]", elemento):
        print(elemento)  # Imprime el pedido si coincide con el patrón