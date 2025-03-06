import sqlite3  # Importa el módulo sqlite3 para trabajar con bases de datos SQLite.

miConexion = sqlite3.connect("Gestion")  # Crea una conexión a una base de datos llamada "Gestion". Si no existe, se creará automáticamente.

miCursor = miConexion.cursor()  # Crea un cursor para ejecutar comandos SQL en la base de datos.

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))              
''')  # Crea una tabla llamada "PRODUCTOS" con cuatro columnas: ID, NOMBRE_ARTICULO, PRECIO y SECCION. La columna ID es la clave primaria y se autoincrementa, mientras que la columna NOMBRE_ARTICULO es única.

productos = [
    ("pelota", 20, "juguetería"),  # Lista de tuplas que representan los productos a insertar en la tabla.
    ("cojín", 15, "moviliario"),
    ("cama", 200, "moviliario"),
    ("destornillador", 5, "herramientas")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)  # Inserta múltiples registros en la tabla "PRODUCTOS" utilizando la lista "productos". Se usa NULL para el ID para que se autoincremente.

miConexion.commit()  # Guarda (confirma) los cambios realizados en la base de datos.

miConexion.close()  # Cierra la conexión a la base de datos.
