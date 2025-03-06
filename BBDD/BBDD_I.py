import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

#variosProductos=[
#
#    ("i9 7900 K", 450, "Tecnología"),
#    ("Nvidia RTX 4080", 1200, "Tecnología"),
#    ("Lápices Prismacolor", 210, "Arte")
#
#]
#
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

print(variosProductos)

for producto in variosProductos:
    print(f"Nombre Artículo: {producto[0]}, Sección: {producto[2]}")

miConexion.commit()


miConexion.close()