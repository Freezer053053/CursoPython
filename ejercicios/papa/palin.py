def es_palindromo(frase):
    caracteres=[]
    for c in frase:
        if c.isalnum():
        #if (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
            caracteres.append(c.lower())

    
    def verificar(caracteres, inicio, fin):
        if inicio>=fin:
            return True
        if caracteres[inicio]!=caracteres[fin]:
            return False
        return verificar(caracteres, inicio+1, fin-1)
    
    return verificar(caracteres, 0, len(caracteres)-1)


frase=input("Introduce una palabra o frase")
print(es_palindromo(frase))
