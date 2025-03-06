import sqlite3  # Importa el módulo sqlite3 para trabajar con bases de datos SQLite.

miConexion = sqlite3.connect("Gestion")  # Crea una conexión a una base de datos llamada "Gestion". Si no existe, se creará automáticamente.

miCursor = miConexion.cursor()  # Crea un cursor para ejecutar comandos SQL en la base de datos.

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='herramientas'")  # Ejecuta una consulta para seleccionar todos los registros de la tabla "PRODUCTOS" donde la sección es 'herramientas'.

productos = miCursor.fetchall()  # Recupera todos los registros obtenidos por la consulta y los almacena en la variable "productos".

print(productos)  # Imprime la lista de todos los registros obtenidos.

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='destornillador'")  # Actualiza el precio del artículo 'destornillador' en la tabla "PRODUCTOS" a 35.

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='herramientas'")  # Ejecuta una consulta para seleccionar todos los registros de la tabla "PRODUCTOS" donde la sección es 'herramientas' nuevamente.

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")  # Elimina el registro de la tabla "PRODUCTOS" donde el ID es 4.

miConexion.commit()  # Guarda (confirma) los cambios realizados en la base de datos.

miConexion.close()  # Cierra la conexión a la base de datos.
