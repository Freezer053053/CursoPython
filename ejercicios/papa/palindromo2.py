def es_palindromo(frase):
    frase_limpia=''.join(frase.split()).lower()
    longitud=len(frase_limpia)

    for i in range(longitud // 2):
        if frase_limpia[i]!=frase_limpia[longitud-i-1]:
            return False
    return True

frase = input("Introduce una palabra o frase: ")
if es_palindromo(frase):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
