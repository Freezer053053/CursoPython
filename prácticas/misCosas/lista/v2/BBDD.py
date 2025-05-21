import sqlite3
from utils import emergentes

miConexion = None
miCursor = None

miConexion=sqlite3.connect("BBDD.db")
miCursor=miConexion.cursor()

def cargar_propiedades_desde_txt(base, txt):
    miConexion = sqlite3.connect(base)
    miCursor = miConexion.cursor()

    # connect(base)

    # Leer el archivo .txt
    with open(f"prácticas/misCosas/lista/{txt}", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    # Determinar qué está leyendo (marcas o tipos)
    match txt:
        case "info_chips.txt":
            cargar_marcas = False
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

def obtener_id_tipo(nombre_tipo):
    """Obtiene el id_tipo dado su nombre en la tabla tipos_componentes."""
    miConexion = sqlite3.connect("BBDD.db")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT id_tipo FROM tipos_componentes WHERE nombre_tipo = ?", (nombre_tipo,))
    resultado = miCursor.fetchone()
    
    miConexion.close()

    return resultado[0] if resultado else None  # Retorna el ID si existe, sino None

def obtener_id_marca(nombre_marca):
    """Obtiene el id_fabricante dado su nombre."""
    miConexion = sqlite3.connect("BBDD.db")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT id_fabricante FROM fabricantes WHERE nombre_fabricante = ?", (nombre_marca,))
    resultado = miCursor.fetchone()
    
    miConexion.close()

    return resultado[0] if resultado else None  # Retorna el ID si existe, sino None

def create():
    miCursor.execute('''

                CREATE TABLE IF NOT EXISTS "usuarios" (
                    "id_usuario" INTEGER NOT NULL UNIQUE,
                    "nombre" VARCHAR NOT NULL,
                    "ApPaterno" VARCHAR,
                    "ApMaterno" VARCHAR,
                    PRIMARY KEY("id_usuario")
                );''')
                     
    miCursor.execute('''

                CREATE TABLE IF NOT EXISTS "componentes" (
                    "id_componente" INTEGER NOT NULL UNIQUE,
                    "nombre" VARCHAR NOT NULL,
                    "id_tipo" INTEGER NOT NULL,
                    "id_fabricante" INTEGER,
                    "cantidad" INTEGER NOT NULL DEFAULT 0,
                    PRIMARY KEY("id_componente"),
                    FOREIGN KEY ("id_tipo") REFERENCES "tipos_componentes"("id_tipo")
                    ON UPDATE NO ACTION ON DELETE NO ACTION,
                    FOREIGN KEY ("id_fabricante") REFERENCES "fabricantes"("id_fabricante")
                    ON UPDATE NO ACTION ON DELETE NO ACTION

                );''')

    miCursor.execute('''


                CREATE TABLE IF NOT EXISTS "diodos" (
                    "id_componente" INTEGER NOT NULL UNIQUE,
                    "tipo_diodo" VARCHAR NOT NULL,
                    "color" VARCHAR,
                    "voltage" REAL,
                    PRIMARY KEY("id_componente"),
                    FOREIGN KEY ("id_componente") REFERENCES "componentes"("id_componente")
                    ON UPDATE NO ACTION ON DELETE NO ACTION
                );''')

    miCursor.execute('''


                CREATE TABLE IF NOT EXISTS "transistores" (
                    "id_componente" INTEGER NOT NULL UNIQUE,
                    "tipo_transistor" VARCHAR NOT NULL,
                    "ganancia" NUMERIC,
                    "voltage_saturación" NUMERIC,
                    "nombre_transistor" VARCHAR NOT NULL,
                    PRIMARY KEY("id_componente"),
                    FOREIGN KEY ("id_componente") REFERENCES "componentes"("id_componente")
                    ON UPDATE NO ACTION ON DELETE NO ACTION
                );''')
                    
    miCursor.execute('''


                CREATE TABLE IF NOT EXISTS "capacitores" (
                    "id_componente" INTEGER NOT NULL UNIQUE,
                    "capacitancia" NUMERIC NOT NULL,
                    "voltage" NUMERIC NOT NULL,
                    "tipo_capacitor" VARCHAR,
                    "polarizado" TEXT NOT NULL CHECK (polarizado IN ("Si", "No")),
                    PRIMARY KEY("id_componente"),
                    FOREIGN KEY ("id_componente") REFERENCES "componentes"("id_componente")
                    ON UPDATE NO ACTION ON DELETE NO ACTION
                );''')
                    
    miCursor.execute('''


                CREATE TABLE IF NOT EXISTS "resistencias" (
                    "id_componente" INTEGER NOT NULL UNIQUE,
                    "resistencia" NUMERIC NOT NULL,
                    "potencia" NUMERIC,
                    "tolerancia" NUMERIC,
                    PRIMARY KEY("id_componente"),
                    FOREIGN KEY ("id_componente") REFERENCES "componentes"("id_componente")
                    ON UPDATE NO ACTION ON DELETE NO ACTION
                );
            ''')

    miCursor.execute('''

                CREATE TABLE IF NOT EXISTS "chips" (
                    "id_componente" INTEGER NOT NULL UNIQUE,
                    "tipo_chip" VARCHAR,
                    "encapsulado" VARCHAR,
                    PRIMARY KEY("id_componente"),
                    FOREIGN KEY ("id_componente") REFERENCES "componentes"("id_componente")
                    ON UPDATE NO ACTION ON DELETE NO ACTION
            );
        ''')

    miCursor.execute('''

                CREATE TABLE IF NOT EXISTS "usuario_componente" (
                    "id_usuario" INTEGER NOT NULL,
                    "id_componente" INTEGER NOT NULL,
                    "cantidad" INTEGER DEFAULT 0,
                    PRIMARY KEY("id_usuario", "id_componente"),
                    FOREIGN KEY ("id_componente") REFERENCES "componentes"("id_componente")
                    ON UPDATE NO ACTION ON DELETE NO ACTION,
                    FOREIGN KEY ("id_usuario") REFERENCES "usuarios"("id_usuario")
                    ON UPDATE NO ACTION ON DELETE NO ACTION
                );
            ''')

    miCursor.execute('''

                CREATE TABLE IF NOT EXISTS "tipos_componentes" (
                    "id_tipo" INTEGER NOT NULL UNIQUE,
                    "nombre_tipo" VARCHAR NOT NULL,
                    PRIMARY KEY("id_tipo")
                );''')

    miCursor.execute('''

                CREATE TABLE IF NOT EXISTS "fabricantes" (
                    "id_fabricante" INTEGER NOT NULL UNIQUE,
                    "nombre_fabricante" VARCHAR NOT NULL,
                    PRIMARY KEY("id_fabricante")
                );


            ''')

    emergentes("creada")
    # miConexion.close()
    loadComponents()

def loadComponents():
    miConexion = sqlite3.connect("BBDD.db")
    miCursor = miConexion.cursor()

    # Obtener los componentes ya existentes
    miCursor.execute("SELECT nombre_tipo FROM tipos_componentes")
    existentes = {fila[0] for fila in miCursor.fetchall()}  # Convertir a conjunto para evitar duplicados

    # Lista de componentes iniciales
    componentes = ["Resistencia", "Capacitor", "Diodo", "Transistor", "IC"]

    # Insertar componentes evitando duplicados
    for componente in componentes:
        if componente not in existentes:  # Solo insertar si no está ya en la tabla
            miCursor.execute("INSERT INTO tipos_componentes (nombre_tipo) VALUES (?);", (componente,))

    # Guardar cambios y cerrar conexión
    miConexion.commit()
    miConexion.close()

    

def obtener_datos_desde_bd(base, tabla, columna):
    miConexion = sqlite3.connect(base)
    miCursor = miConexion.cursor()
    query = f"SELECT {columna} FROM {tabla}"

    try:
        miCursor.execute(query)
        datos = [fila[0] for fila in miCursor.fetchall()]
        return datos
    except Exception as e:
        print(f"Error al consultar {tabla}.{columna} en {base}:", e)
        return []

def createUser(tabla, datos, columnas_clave):
    try:
        
        # Si no existe, insertar una nueva fila
        columnas = ", ".join(datos.keys())
        valores = ", ".join(["?"] * len(datos))
        query_insertar = f"INSERT INTO {tabla} ({columnas}) VALUES ({valores})"
        miCursor.execute(query_insertar, tuple(datos.values()))
        filas_afectadas = miCursor.rowcount  # Verificar filas insertadas

        miConexion.commit()

        # Verificar si se afectaron filas
        if filas_afectadas > 0:
            print(f"{tabla} - Usuario insertado correctamente: {datos}")
            return True
        else:
            print(f"{tabla} - No se pudo insertar el usuario: {datos}")
            return False

    except Exception as e:
        print(f"Error al insertar el usuario: {e}")
        return False

def eraseUser(nombre_usuario):
    # Verificar si el usuario existe
     
    miConexion = sqlite3.connect("BBDD.db")
    miCursor = miConexion.cursor()

    # Eliminar el usuario de la base de datos
    miCursor.execute("DELETE FROM usuarios WHERE nombre=?", (nombre_usuario,))
    miConexion.commit()
    miConexion.close()