import sqlite3

miConexion = None
miCursor = None



def obtener_datos_desde_bd(base, tabla, columna):
    miConexion = sqlite3.connect(base)
    miCursor = miConexion.cursor()
    connect(base)  # Conecta a la base especificada
    query = f"SELECT {columna} FROM {tabla}"
    try:
        miCursor.execute(query)
        datos = [fila[0] for fila in miCursor.fetchall()]
        return datos
    except Exception as e:
        print(f"Error al consultar {tabla}.{columna} en {base}:", e)
        return []



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
                    # cargar_marcas = False
                    cargar_tipos = True
                    cargar_encapsulados = False
                    continue
                elif linea.lower() == "encapsulados:":
                    # cargar_marcas = False
                    cargar_tipos = False
                    cargar_encapsulados = True
                    continue
                
                # Insertar en la tabla correspondiente
                # if cargar_marcas and linea != "":
                #     miCursor.execute("INSERT OR IGNORE INTO MARCAS (MARCA) VALUES (?)", (linea,))
                #     miCursor.execute("DELETE FROM MARCAS WHERE MARCA IS NULL OR MARCA = '';")
                if cargar_tipos and linea != "":
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


def check_connection():
    global miConexion
    global miCursor

    try:
        miCursor.execute("SELECT 1")
        return True
    except AttributeError as e:
        pass

def createTableAllComponents(base):
    try:
        connect(base)  # Conectar a la base específica
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS TIPOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TIPO TEXT UNIQUE
            )
        ''')
        miConexion.commit()
        print("Tabla creada correctamente")
    except Exception as e:
        print("Error al crear tabla:", e)

def createTableIC(base):
    try:
        connect(base)  # Conectar a la base específica
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS MARCAS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                MARCA TEXT UNIQUE
            )
        ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS TIPOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TIPO TEXT UNIQUE
            )
        ''')
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS ENCAPSULADOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ENCAPSULADO TEXT UNIQUE
            )
        ''')
        miConexion.commit()
        print("Tablas de IC creadas correctamente en:", base)
    except Exception as e:
        print("Error al crear tablas IC:", e)


def createTableTR(base):
    try:

        connect(base)

        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS TIPOS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TIPO TEXT UNIQUE
        )         
    ''')
        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS ENCAPSULADOS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ENCAPSULADO TEXT UNIQUE
        )         
    ''')
        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS PATILLAGES
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PATILLAGE TEXT UNIQUE
        )         
    ''')
        miConexion.commit()
        print("Tablas de transistores creadas correctamente")
        print("Conectado a las tablas de transistores")
    except:
        print("No se pudo realizar")

def createTableCP(base):
    try:

        connect(base)

        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS TIPOS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TIPO TEXT UNIQUE
        )         
        ''')
        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS POLARIZADOS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        POLARIZADO TEXT UNIQUE
        )         
    ''')
        miConexion.commit()
        print("Tablas de capacitores creadas correctamente")
        print("Conectado a las tablas de capacitores")
    except:
        print("No se pudo realizar")
        
def createTableDI(base):
    try:

        connect(base)

        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS TIPOS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TIPO TEXT UNIQUE
        )         
        ''')
        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS TIPOS_SIN_COLORES
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TIPO TEXT UNIQUE
        )         
        ''')
        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS COLORES
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        COLOR TEXT UNIQUE
        )         
    ''')
        miConexion.commit()
        print("Tablas de diodos creadas correctamente")
        print("Conectado a las tablas de diodos")
    except:
        print("No se pudo realizar")

def createTableR(base):
    try:

        connect(base)

        miCursor.execute('''
        CREATE TABLE IF NOT EXISTS TIPOS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TIPO TEXT UNIQUE
        )         
        ''')

        miConexion.commit()
        print("Tablas de resistencias creadas correctamente")
        print("Conectado a las tablas de resistencias")
    except:
        print("Conectado a las tablas")

def connect(base):
    global miConexion
    global miCursor

    if check_connection():
        print("Actualmente ya estás conectado a la BBDD")
    else:
        miConexion = sqlite3.connect(base)
        miCursor = miConexion.cursor()
        if check_connection():
            print("Conexión establecida con éxito en:", base)
            
            # Crear tablas según el tipo de base
            if "chips.db" in base:
                createTableIC(base)
            elif "transistores.db" in base:
                createTableTR(base)
            elif "capacitores.db" in base:
                createTableCP(base)
            elif "diodos.db" in base:
                createTableDI(base)
            elif "resistencias.db" in base:
                createTableR(base)
            elif "all_components.db" in base:
                createTableAllComponents(base)
        else:
            print("Conexión fallida en:", base)


# connect()