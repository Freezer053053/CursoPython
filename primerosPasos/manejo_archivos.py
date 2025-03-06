from io import open

archivo_texto=open("archivo.txt","w")

frase="Estupendo día para python\nen el día de hoy"

archivo_texto.write(frase)

archivo_texto=open("archivo.txt","r")

texto=archivo_texto.read()

print(texto)

archivo_texto=open("archivo.txt", "a")

archivo_texto.write("\nsiempre es una buena ocasion")

archivo_texto=open("archivo.txt","r")

archivo_texto.seek(0)

print(texto)

archivo_texto.close()