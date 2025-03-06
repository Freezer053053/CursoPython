import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))              
''')

productos=[

    ("AA00", "pelota", 20, "juguetería"),
    ("AA01", "cojín", 15, "moviliario"),
    ("AA02", "cama", 200, "moviliario"),
    ("AA03", "destornillador", 5, "herramientas")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)




miConexion.commit()

miConexion.close()