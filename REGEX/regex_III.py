import re  # Importa el módulo de expresiones regulares

# Define una lista de URLs
lista_URLs = [
    "http://pildorasinformaticas.es",
    "ftp://pildorasinformaticas.es",
    "http://pildorasinformaticas.com",
    "ftp://pildorasinformaticas.com"
]

# Itera sobre cada elemento en la lista de URLs
for elemento in lista_URLs:
    # Busca URLs que terminen con ".es"
    if re.findall(".es$", elemento):
        print(elemento)  # Imprime la URL si termina con ".es"

# Itera nuevamente sobre cada elemento en la lista de URLs
for elemento in lista_URLs:
    # Busca URLs que comiencen con "ftp"
    if re.findall("^ftp", elemento):
        print(elemento)  # Imprime la URL si comienza con "ftp"

# Itera nuevamente sobre cada elemento en la lista de URLs
for elemento in lista_URLs:
    # Busca URLs que contengan la letra "c"
    if re.findall("[c]", elemento):
        print(elemento)  # Imprime la URL si contiene la letra "c"

# Define una lista genérica de palabras
lista_generica = [
    "Hombres",
    "Mujeres",
    "Mascotas",
    "Niños",
    "Niñas",
    "Camión",
    "Camion"
]

# Itera sobre cada elemento en la lista genérica
for elemento in lista_generica:
    # Busca palabras que coincidan con "Niños" o "Niñas"
    if re.findall("Niñ[ao]s", elemento):
        print(elemento)  # Imprime la palabra si coincide con "Niños" o "Niñas"

# Itera nuevamente sobre cada elemento en la lista genérica
for elemento in lista_generica:
    # Busca palabras que coincidan con "Camión" o "Camion"
    if re.findall("Cami[oó]n", elemento):
        print(elemento)  # Imprime la palabra si coincide con "Camión" o "Camion"