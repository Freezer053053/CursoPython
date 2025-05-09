import sqlite3
from utils import emergentes

miConexion = None
miCursor = None

miConexion=sqlite3.connect("BBDD.db")
miCursor=miConexion.cursor()
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
                    "nombre_chip" VARCHAR NOT NULL,
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
