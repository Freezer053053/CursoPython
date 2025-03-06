import sqlite3  # Importa el módulo sqlite3 para trabajar con bases de datos SQLite.

miConexion = sqlite3.connect("GestionProductos")  # Crea una conexión a una base de datos llamada "GestionProductos". Si no existe, se creará automáticamente.

miCursor = miConexion.cursor()  # Crea un cursor para ejecutar comandos SQL en la base de datos.

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))              
''')  # Crea una tabla llamada "PRODUCTOS" con cuatro columnas: CODIGO_ARTICULO, NOMBRE_ARTICULO, PRECIO y SECCION. La columna CODIGO_ARTICULO es la clave primaria.

productos = [
    ("AA00", "pelota", 20, "juguetería"),  # Lista de tuplas que representan los productos a insertar en la tabla.
    ("AA01", "cojín", 15, "moviliario"),
    ("AA02", "cama", 200, "moviliario"),
    ("AA03", "destornillador", 5, "herramientas")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)  # Inserta múltiples registros en la tabla "PRODUCTOS" utilizando la lista "productos".

miConexion.commit()  # Guarda (confirma) los cambios realizados en la base de datos.

miConexion.close()  # Cierra la conexión a la base de datos.
