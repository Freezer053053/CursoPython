import sqlite3
from io import open
from utils import emergentes

miConexion = None
miCursor = None

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

def createTable():
    try:
        miCursor.execute('''
                         CREATE TABLE Capacitores (
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         tipo TEXT,
                         polarizado TEXT NOT NULL CHECK (polarizado IN ("Si", "No")),
                         capacitancia DECIMAL,
                         voltios DECIMAL,
                         cantidad REAL
                         )
                         ''')
        
        miCursor.execute('''
                         CREATE TABLE Diodos (
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         tipo TEXT,
                         color TEXT,
                         voltios DECIMAL,
                         cantidad INTEGER
                         )
                         ''')
        
        miCursor.execute('''
                         CREATE TABLE Resistencias (
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         tipo TEXT,
                         valor DECIMAL,
                         cantidad INTEGER
                         )
                         ''')
        
        miCursor.execute('''
                         CREATE TABLE Chips (
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         marca TEXT,
                         tipo TEXT,
                         encapsulado TEXT,
                         modelo TEXT,
                         cantidad INTEGER
                         )
                         ''')
        
        miCursor.execute('''
                         CREATE TABLE Transistores (
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         tipo TEXT,
                         patillage TEXT,
                         encapsulado TEXT,
                         modelo TEXT,
                         cantidad INTEGER
                         )
                         ''')
        emergentes("tablas creadas")
        emergentes("conectado")
    except:
        emergentes("conectado")
    #borrar()

def connect(user):
    if check_connection():
        emergentes("ya conectado")
    else:
        global miConexion
        global miCursor
        miConexion=sqlite3.connect(f"Componentes_{user}.db")
        miCursor=miConexion.cursor()

        if (check_connection()):
            emergentes("conectar")
            createTable()
        else:
            emergentes("no se pudo conectar")
            
def agregar(componente):

    match componente:
        case "condensador":
            datos =[]
            miCursor.execute("INSERT INTO Capacitores VALUES (NULL,?,?,?,?,?)", datos)

def contenido():
    try:
        componentes = {}
        
        # Tablas a consultar
        tablas = ["transistores", "Chips", "diodos", "resistencias", "capacitores"]
        
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
