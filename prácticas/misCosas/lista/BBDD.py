import sqlite3
from io import open
from utils import emergentes

miConexion = None
miCursor = None

def cargar_propiedades_desde_txt(base, txt):
    miConexion = sqlite3.connect(base)
    miCursor = miConexion.cursor()

    connect(base)

    # Leer el archivo .txt
    with open(f"prácticas/misCosas/lista/{txt}", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    # Determinar qué está leyendo (marcas o tipos)
    match txt:
        case "info_chips.txt":
            # cargar_marcas = False
            cargar_tipos = False
            cargar_encapsulados = False

            for linea in lineas:
                linea = linea.strip()
                if linea.lower() == "marcas:":
                    cargar_marcas = True
                    cargar_tipos = False
                    cargar_encapsulados = False
                    continue
                elif linea.lower() == "tipos:":
                    cargar_marcas = False
                    cargar_tipos = True
                    cargar_encapsulados = False
                    continue
                elif linea.lower() == "encapsulados:":
                    cargar_marcas = False
                    cargar_tipos = False
                    cargar_encapsulados = True
                    continue
                
                # Insertar en la tabla correspondiente
                if cargar_marcas and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO fabricantes (nombre_fabricante) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM fabricantes WHERE nombre_fabricante IS NULL OR nombre_fabricante = '';")
                elif cargar_tipos and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO TIPOS (TIPO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM TIPOS WHERE TIPO IS NULL OR TIPO = '';")
                elif cargar_encapsulados and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO ENCAPSULADOS (ENCAPSULADO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM ENCAPSULADOS WHERE ENCAPSULADO IS NULL OR ENCAPSULADO = '';")

            miConexion.commit()
            miConexion.close()
            print("Conexión cerrada")
        
        case "info_transistores.txt":
            cargar_tipos = False
            cargar_encapsulados = False
            cargar_patillages = False

            for linea in lineas:
                linea = linea.strip()
                if linea.lower() == "tipos:":
                    cargar_tipos = True
                    cargar_encapsulados = False
                    cargar_patillages = False
                    continue
                elif linea.lower() == "encapsulados:":
                    cargar_tipos = False
                    cargar_encapsulados = True
                    cargar_patillages = False
                    continue
                elif linea.lower() == "patillages:":
                    cargar_tipos = False
                    cargar_encapsulados = False
                    cargar_patillages = True
                    continue
                
                # Insertar en la tabla correspondiente
                if cargar_tipos and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO TIPOS (TIPO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM TIPOS WHERE TIPO IS NULL OR TIPO = '';")
                elif cargar_patillages and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO ENCAPSULADOS (ENCAPSULADO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM ENCAPSULADOS WHERE ENCAPSULADO IS NULL OR ENCAPSULADO = '';")
                elif cargar_encapsulados and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO PATILLAGES (PATILLAGE) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM PATILLAGES WHERE PATILLAGE IS NULL OR PATILLAGE = '';")

            miConexion.commit()
            miConexion.close()
            print("Conexión cerrada")

        case "info_capacitores.txt":
            cargar_tipos = False
            cargar_polarizados = False

            for linea in lineas:
                linea = linea.strip()
                if linea.lower() == "tipos:":
                    cargar_tipos = True
                    cargar_polarizados = False
                    continue
                elif linea.lower() == "polarizados:":
                    cargar_tipos = False
                    cargar_polarizados = True
                    continue

                # Insertar en la tabla correspondiente
                if cargar_tipos and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO TIPOS (TIPO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM TIPOS WHERE TIPO IS NULL OR TIPO = '';")
                elif cargar_polarizados and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO POLARIZADOS (POLARIZADO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM POLARIZADOS WHERE POLARIZADO IS NULL OR POLARIZADO = '';")

            miConexion.commit()
            miConexion.close()
            print("Conexión cerrada")
        
        case "info_diodos.txt":
            cargar_tipos = False
            cargar_tipos_sin_colores = False
            cargar_colores = False

            for linea in lineas:
                linea = linea.strip()
                if linea.lower() == "tipos:":
                    cargar_tipos = True
                    cargar_tipos_sin_colores = False
                    cargar_colores = False
                    continue
                elif linea.lower() == "tipos_sin_colores:":
                    cargar_tipos = False
                    cargar_tipos_sin_colores = True
                    cargar_colores = False
                    continue
                elif linea.lower() == "colores:":
                    cargar_tipos = False
                    cargar_tipos_sin_colores = False
                    cargar_colores = True
                    continue

                # Insertar en la tabla correspondiente
                if cargar_tipos and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO TIPOS (TIPO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM TIPOS WHERE TIPO IS NULL OR TIPO = '';")
                elif cargar_tipos_sin_colores and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO TIPOS_SIN_COLORES (TIPO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM TIPOS_SIN_COLORES WHERE TIPO IS NULL OR TIPO = '';")
                elif cargar_colores and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO COLORES (COLOR) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM COLORES WHERE COLOR IS NULL OR COLOR = '';")

            miConexion.commit()
            miConexion.close()
            print("Conexión cerrada")

        case "info_resistencias.txt":
            cargar_tipos = False

            for linea in lineas:
                linea = linea.strip()
                if linea.lower() == "tipos:":
                    cargar_tipos = True
                    continue

                # Insertar en la tabla correspondiente
                if cargar_tipos and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO TIPOS (TIPO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM TIPOS WHERE TIPO IS NULL OR TIPO = '';")

            miConexion.commit()
            miConexion.close()
            print("Conexión cerrada")

        case "componentes.txt":
            cargar_tipos = False

            for linea in lineas:
                linea = linea.strip()
                if linea.lower() == "componentes:":
                    cargar_tipos = True
                    continue

                # Insertar en la tabla correspondiente
                if cargar_tipos and linea != "":
                    miCursor.execute("INSERT OR IGNORE INTO TIPOS (TIPO) VALUES (?)", (linea,))
                    miCursor.execute("DELETE FROM TIPOS WHERE TIPO IS NULL OR TIPO = '';")

            miConexion.commit()
            miConexion.close()
            print("Conexión cerrada")

def insertar_o_actualizar_componente(tabla, datos, columnas_clave):
    try:
        # Filtrar las columnas clave según los valores relevantes (eliminar columnas con valores None)
        columnas_clave_validas = [col for col in columnas_clave if datos.get(col) is not None]
        where_clause = " AND ".join([f"{col} = ?" for col in columnas_clave_validas])
        valores_where = [datos[col] for col in columnas_clave_validas]

        # Consultar si ya existe el componente
        query_buscar = f"SELECT cantidad FROM {tabla} WHERE {where_clause}"
        miCursor.execute(query_buscar, tuple(valores_where))
        resultado = miCursor.fetchone()

        if resultado:
            # Si el componente ya existe, actualizar la cantidad
            nueva_cantidad = int(resultado[0]) + int(datos["cantidad"])
            query_actualizar = f"UPDATE {tabla} SET cantidad = ? WHERE {where_clause}"
            miCursor.execute(query_actualizar, (nueva_cantidad, *valores_where))
            filas_afectadas = miCursor.rowcount  # Verificar filas actualizadas
        else:
            # Si no existe, insertar una nueva fila
            columnas = ", ".join(datos.keys())
            valores = ", ".join(["?"] * len(datos))
            query_insertar = f"INSERT INTO {tabla} ({columnas}) VALUES ({valores})"
            miCursor.execute(query_insertar, tuple(datos.values()))
            filas_afectadas = miCursor.rowcount  # Verificar filas insertadas

        miConexion.commit()

        # Verificar si se afectaron filas
        if filas_afectadas > 0:
            print(f"{tabla} - Componente actualizado o insertado correctamente: {datos}")
            return True
        else:
            print(f"{tabla} - No se pudo insertar ni actualizar el componente: {datos}")
            return False

    except Exception as e:
        print(f"Error al insertar o actualizar datos: {e}")
        return False




def check_connection():
    global miConexion
    global miCursor

    try:
        miCursor.execute("SELECT 1")
        return True
    except AttributeError as e:
        pass

# def createTable():
#     try:
#         miCursor.execute('''
#                          CREATE TABLE Capacitores (
#                          ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                          tipo TEXT,
#                          polarizado TEXT NOT NULL CHECK (polarizado IN ("Si", "No")),
#                          capacitancia DECIMAL,
#                          voltios DECIMAL,
#                          cantidad REAL
#                          )
#                          ''')
        
#         miCursor.execute('''
#                          CREATE TABLE Diodos (
#                          ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                          tipo TEXT,
#                          color TEXT,
#                          voltios DECIMAL,
#                          cantidad INTEGER
#                          )
#                          ''')
        
#         miCursor.execute('''
#                          CREATE TABLE Resistencias (
#                          ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                          tipo TEXT,
#                          valor DECIMAL,
#                          cantidad INTEGER
#                          )
#                          ''')
        
#         miCursor.execute('''
#                          CREATE TABLE Chips (
#                          ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                          marca TEXT,
#                          tipo TEXT,
#                          encapsulado TEXT,
#                          modelo TEXT,
#                          cantidad INTEGER
#                          )
#                          ''')
        
#         miCursor.execute('''
#                          CREATE TABLE Transistores (
#                          ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                          tipo TEXT,
#                          patillage TEXT,
#                          encapsulado TEXT,
#                          modelo TEXT,
#                          cantidad INTEGER
#                          )
#                          ''')
#         emergentes("tablas creadas")
#         emergentes("conectado")
#     except:
#         emergentes("conectado")
#     #borrar()

def connect(user):
    if user is not "":
        if check_connection():
            emergentes("ya conectado")
        else:
            global miConexion
            global miCursor
            miConexion=sqlite3.connect("BBDD.db")
            miCursor=miConexion.cursor()

            if (check_connection()):
                emergentes("conectar")
                print(f"conectado como {user}")
                # print(type(user))
                createTable()
            else:
                emergentes("no se pudo conectar")
    else:
        emergentes("no_usuario")

def desconectar():
    try:
        miConexion.close()
        emergentes("desconectar")
    
    except AttributeError:
        emergentes("no_conectado")
            
def agregar(componente):

    match componente:
        case "condensador":
            datos =[]
            miCursor.execute("INSERT INTO Capacitores VALUES (NULL,?,?,?,?,?)", datos)

def contenido():
    try:
        componentes = {}
        
        # Tablas a consultar
        tablas = ["transistores", "chips", "diodos", "resistencias", "capacitores"]
        
        for tabla in tablas:
            query = f"SELECT * FROM {tabla}"
            miCursor.execute(query)
            resultados = miCursor.fetchall()
            
            if resultados:
                componentes[tabla] = resultados
        
        return componentes
    except Exception as e:
        print(f"Error al recuperar componentes: {e}")
        return None
