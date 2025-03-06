import sqlite3  # Importa el módulo sqlite3 para trabajar con bases de datos SQLite.

miConexion = sqlite3.connect("PrimeraBase")  # Crea una conexión a una base de datos llamada "PrimeraBase". Si no existe, se creará automáticamente.

miCursor = miConexion.cursor()  # Crea un cursor para ejecutar comandos SQL en la base de datos.

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")  # Crea una tabla llamada "PRODUCTOS" con tres columnas: NOMBRE_ARTICULO, PRECIO y SECCION (comentado).

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")  # Inserta un registro en la tabla "PRODUCTOS" (comentado).

# variosProductos = [  # Crea una lista de varios productos con sus respectivos valores (comentado).
#    ("i9 7900 K", 450, "Tecnología"),
#    ("Nvidia RTX 4080", 1200, "Tecnología"),
#    ("Lápices Prismacolor", 210, "Arte")
# ]
#
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)  # Inserta múltiples registros en la tabla "PRODUCTOS" utilizando la lista "variosProductos" (comentado).

miCursor.execute("SELECT * FROM PRODUCTOS")  # Ejecuta una consulta para seleccionar todos los registros de la tabla "PRODUCTOS".

variosProductos = miCursor.fetchall()  # Recupera todos los registros obtenidos por la consulta y los almacena en la variable "variosProductos".

print(variosProductos)  # Imprime la lista de todos los registros obtenidos.

for producto in variosProductos:  # Itera a través de cada registro en la lista "variosProductos".
    print(f"Nombre Artículo: {producto[0]}, Sección: {producto[2]}")  # Imprime el nombre del artículo y la sección para cada registro.

miConexion.commit()  # Guarda (confirma) los cambios realizados en la base de datos.

miConexion.close()  # Cierra la conexión a la base de datos.
