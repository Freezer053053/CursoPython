import re  # Importa el módulo de expresiones regulares

# Define una cadena de texto para analizar
cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguage de sintaxis sencilla"

# Define el texto que se va a buscar en la cadena
texto_buscar = "aprender"

# Realiza la búsqueda del texto en la cadena
textoEncontrado = re.search(texto_buscar, cadena)

# Si se encuentra el texto, imprime la posición inicial
print(textoEncontrado.start())  # Imprime la posición inicial de "aprender"

# Imprime la posición final del texto encontrado
print(textoEncontrado.end())  # Imprime la posición final de "aprender"

# Imprime una tupla con las posiciones inicial y final del texto encontrado
print(textoEncontrado.span())  # Imprime (posición inicial, posición final) de "aprender"

# Cambia el texto a buscar a "Python"
texto_buscar = "Python"

# Busca todas las apariciones de "Python" en la cadena y cuenta cuántas veces aparece
print(len(re.findall(texto_buscar, cadena)))  # Imprime el número de veces que "Python" aparece en la cadena