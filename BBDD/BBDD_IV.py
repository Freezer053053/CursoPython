import sqlite3

miConexion=sqlite3.connect("Gestion")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='herramientas'")

productos=miCursor.fetchall()

print(productos)

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='destornillador'")

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='herramientas'")  

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4") 

miConexion.commit()

miConexion.close()