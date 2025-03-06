import sqlite3

miConexion=sqlite3.connect("Gestion")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))              
''')

productos=[

    ("pelota", 20, "juguetería"),
    ("cojín", 15, "moviliario"),
    ("cama", 200, "moviliario"),
    ("destornillador", 5, "herramientas")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)




miConexion.commit()

miConexion.close()