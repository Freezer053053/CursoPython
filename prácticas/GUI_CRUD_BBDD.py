from tkinter import *
from tkinter import messagebox
import sqlite3


#-------------------------------------------FUNCIONES-------------------------------------------#
miCursor=None
miConexion=None

def ayuda():
    messagebox.showwarning("Estado", "Tenga en cuenta que las instrucciones aun estan inacabadas")
    messagebox.showinfo("Uso de la applicación",
                        '''
                        Para conectarse a la BBDD usted tiene que ir al menú BBDD y hacer click en conectar a BBDD.\nLos valores introducidos en los campos 'nombre' y 'apellido' tienen que comenzar en mayúsculas.\nPara ver el contenido de la tabla introduce el ID y haz click en 'read' o en 'CRUD>Leer'.\nAsegurate de que antes de salir siempre cierres la conexión con la base de datos en el menú 'BBDD>Desconectar de BBDD'...''')

def avisoLicencia():
    messagebox.showinfo("Licencia", "Producto bajo licencia MisHuevos33")

def con_numeros(texto):
    return any(char.isdigit() for char in texto)

def check_connection():
    global miConexion
    global miCursor

    try:
        miCursor.execute("SELECT 1")
        return True
    except AttributeError as e:
        pass


def connect():
    if check_connection():
        info=messagebox.showerror("Error", "Actualmente ya estás conectado a la BBDD")
    else:
        global miConexion
        global miCursor
        miConexion=sqlite3.connect("Gestion")
        miCursor=miConexion.cursor()

        if (check_connection()):
            info=messagebox.showinfo("Conectar", "Conexión establecida con éxito")
            createTable()
        else:
            info=messagebox.showerror("Error", "Conexión fallida")

def createTable():
    try:
        miCursor.execute('''
        CREATE TABLE PERSONAS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE TEXT,
        APELLIDO TEXT,
        CONTRASEÑA TEXT,
        DIRECCION TEXT,
        COMENTARIOS TEXT)         
    ''')
        info=messagebox.showinfo("Info", "Tabla personas creada correctamente")
        info=messagebox.showinfo("Info", "Conectado a tabla existente: pesonas")
    except:
        info=messagebox.showinfo("Info", "Conectado a tabla existente: pesonas")
    borrar()

def create():

    if check_connection():
        clave=campoID.get()
        nombre=campoNombre.get()
        apellido=campoApellido.get()
        password=campoPassw.get()
        direccion=campoDir.get()
        comentarios=textoComentarios.get('1.0', END)
        #print(comentarios)

        nombre=nombre.title()
        apellido=apellido.title()

        if (nombre=="" or apellido=="" or password=="" or direccion==""):
            info=messagebox.showerror("Error", "Rellene los campos faltantes")
        elif (con_numeros(nombre) or con_numeros(apellido) or nombre.isalnum()==False or apellido.isalnum()==False):
            info=messagebox.showerror("Error", "No se admiten numeros u otros caracteres especiales en los campos 'Nombre' y 'Apellido'")
        elif (clave!=""):
            info=messagebox.showwarning("Campo ID", "No puedes asignar un ID manualmente. Limpia el campo ID")
        else:
            datos=[nombre, apellido, password, direccion, comentarios] 
            miCursor.execute("INSERT INTO PERSONAS VALUES (NULL,?,?,?,?,?)", datos)
            info=messagebox.showinfo("Exito", "Datos creados con éxito!")
            miConexion.commit()

    else:
        info=messagebox.showerror("Error", "No estas conectado a ninguna base de datos.\nConéctate desde el menú BBDD\nPara mas información abra el menú ayuda y seleccione 'Como usar el programa'")

def actualizar():
    if check_connection():
        try:
            clave=campoID.get()
            nombre=campoNombre.get()
            apellido=campoApellido.get()
            password=campoPassw.get()
            direccion=campoDir.get()
            comentarios=textoComentarios.get('1.0', END)

            if (clave=="" or nombre=="" or apellido=="" or password=="" or direccion==""):
                info=messagebox.showerror("Error", "Rellene todos los campos para actualizar")
            elif (con_numeros(nombre) or con_numeros(apellido)):
                info=messagebox.showerror("Error", "No se admiten números en los campos 'Nombre' y 'Apellido'")
            else:
                miCursor.execute("SELECT COUNT(*) FROM PERSONAS WHERE ID=?", (clave,))
                if miCursor.fetchone()[0]==0:
                    info=messagebox.showerror("Error", "El ID seleccionado no existe en la tabla")
                else:
                    datos=[nombre.title(), apellido.title(), password, direccion, comentarios, clave]
                    miCursor.execute("UPDATE PERSONAS SET NOMBRE=?, APELLIDO=?, CONTRASEÑA=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?", datos)
                    miConexion.commit()
                    info=messagebox.showinfo("Éxito", "Datos actualizados con éxito!")
        except Exception as e:
            info=messagebox.showerror("Error", f"Error al actualizar los datos: {e}")
    else:
        info=messagebox.showerror("Error", "No estás conectado a ninguna base de datos. Conéctate desde el menú BBDD\nPAra mas información abra el menú ayuda y seleccione 'Como usar el programa'")
        
def leer():
    clave=campoID.get()
    borrar()

    try:
        #print(clave)
        miCursor.execute("SELECT NOMBRE FROM PERSONAS WHERE ID=?", (clave,))
        nombre_datos=miCursor.fetchone()
        miCursor.execute("SELECT APELLIDO FROM PERSONAS WHERE ID=?", (clave,))
        apellido_datos=miCursor.fetchone()
        miCursor.execute("SELECT CONTRASEÑA FROM PERSONAS WHERE ID=?", (clave,))
        password_datos=miCursor.fetchone()
        miCursor.execute("SELECT DIRECCION FROM PERSONAS WHERE ID=?", (clave,))
        direccion_datos=miCursor.fetchone()
        miCursor.execute("SELECT COMENTARIOS FROM PERSONAS WHERE ID=?", (clave,))
        comentarios_datos=miCursor.fetchone()

        identificacion.set(clave)
        nombre.set(nombre_datos[0])
        apellido.set(apellido_datos[0])
        password.set(password_datos[0])
        direccion.set(direccion_datos[0])
        textoComentarios.insert(END, comentarios_datos[0])

        miConexion.commit()

    except IndexError:
        info=messagebox.showerror("Error", "No existen datos para esta clave")
    except AttributeError:
        info=messagebox.showerror("Error", "No estas conectado a ninguna base de datos.\nConéctate desde el menú BBDD\nPAra mas información abra el menú ayuda y seleccione 'Como usar el programa'")
    
    except TypeError:
        if clave=="":
            info=messagebox.showerror("Error", "Introduzca el campo ID a buscar")
        elif clave<="0":
            info=messagebox.showerror("Error", "Introduzca un ID válido")
        else:
            info=messagebox.showerror("Error", "El campo ID seleccionado no existe")

def borrar():
    identificacion.set("")
    nombre.set("")
    apellido.set("")
    password.set("")
    direccion.set("")
    textoComentarios.delete('1.0', END)

def salir():
    valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicación?")
    if valor:
        try:
            if check_connection():
                print("Cerrando conexión")
                info=messagebox.showinfo("Conexión", "Conexión a BBDD cerrada con éxito")
                miConexion.close()
                root.destroy()
            else:
                root.destroy()
        except:
            root.destroy()

def desconectar():
    try:
        miConexion.close()
        info=messagebox.showinfo("Desconectar", "Desconectado de la BBDD con éxito")
    
    except AttributeError:
        info=messagebox.showinfo("Info", "Aún no estas conectado a la BBDD")

def delete():
    clave=campoID.get()

    try:
        miCursor.execute("DELETE FROM PERSONAS WHERE ID=?", (clave,))
        
        if miCursor.rowcount==0:
            info=messagebox.showerror("Error", "El campo ID seleccionado no existe")
        elif clave=="":
            info=messagebox.showerror("Error", "Introduzca el campo ID a buscar")
        elif clave<="0":
            info=messagebox.showerror("Error", "Introduzca un ID válido")
        else:
            miConexion.commit()

    except AttributeError:
        info=messagebox.showerror("Error", "No estás conectado a ninguna base de datos.\nConéctate desde el menú BBDD\nPAra mas información abra el menú ayuda y seleccione 'Como usar el programa'")

    

#-------------------------------------------GUI-------------------------------------------#

root=Tk()
root.resizable(0, 0)

identificacion=IntVar()
nombre=StringVar()
apellido=StringVar()
password=StringVar()
direccion=StringVar()
comentarios=StringVar()

barraMenu=Menu(root)
BBDDMenu=Menu(barraMenu, tearoff=0)
borrarMenu=Menu(barraMenu, tearoff=0)
CRUDMenu=Menu(barraMenu, tearoff=0)
ayudaMenu=Menu(barraMenu, tearoff=0)

root.config(menu=barraMenu, width=250, height=400)
#root.resizable(0,0)
#root.geometry("250x400")
root.title("Gestión BBDD")

#-------------------------------------------MENU_SUPERIOR-------------------------------------------#

barraMenu.add_cascade(label="BBDD", menu=BBDDMenu)
BBDDMenu.add_command(label="Conectar a BBDD", command=lambda:connect())
BBDDMenu.add_command(label="Desconectar de BBDD", command=lambda:desconectar())
BBDDMenu.add_separator()
BBDDMenu.add_command(label="Salir", command=lambda:salir())

barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
borrarMenu.add_command(label="Borrar campos", command=lambda:borrar())

barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
CRUDMenu.add_command(label="Crear", command=lambda:create())
CRUDMenu.add_command(label="Leer", command=lambda:leer())
CRUDMenu.add_command(label="Actualizar", command=lambda:actualizar())
CRUDMenu.add_command(label="Eliminar", command=lambda:delete())

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label="Licencia", command=lambda:avisoLicencia())
ayudaMenu.add_command(label="Como usar el programa", command=lambda:ayuda())

#-------------------------------------------CREACIÓN_DEL_FRAME-------------------------------------------#

miFrame=Frame(root, width=250, height=400)
miFrame.pack()

#miFrame.config(bg="blue")

#-------------------------------------------CAMPOS_FRAME-------------------------------------------#

campoID=Entry(miFrame, textvariable=identificacion)
campoID.grid(row=0, column=1, pady=5, padx=10, columnspan=3)

IDLabel=Label(miFrame, text="ID: ")
IDLabel.grid(row=0, column=0, sticky="e")

#---------------------------------------------------

campoNombre=Entry(miFrame, textvariable=nombre)
campoNombre.grid(row=1, column=1, pady=5, padx=10, columnspan=3)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e")

#---------------------------------------------------

campoApellido=Entry(miFrame, textvariable=apellido)
campoApellido.grid(row=2, column=1, pady=5, padx=10, columnspan=3)
apellidoLabel=Label(miFrame, text="1er Apellido: ")

apellidoLabel.grid(row=2, column=0, sticky="e")

#---------------------------------------------------

campoPassw=Entry(miFrame, textvariable=password)
campoPassw.grid(row=3, column=1, pady=5, padx=10, columnspan=3)
campoPassw.config(show="*")

passwLabel=Label(miFrame, text="Password: ")
passwLabel.grid(row=3, column=0, sticky="e")

#---------------------------------------------------

campoDir=Entry(miFrame, textvariable=direccion)
campoDir.grid(row=4, column=1, pady=5, padx=10, columnspan=3)

dirLabel=Label(miFrame, text="Dirección: ")
dirLabel.grid(row=4, column=0, sticky="e")

#---------------------------------------------------

textoComentarios=Text(miFrame, width=16, height=5)
textoComentarios.grid(row=5, column=1, pady=5, padx=10, columnspan=3)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e")

scrollVert=Scrollbar(miFrame, command=textoComentarios.yview)
scrollVert.grid(row=5, column=4, sticky=NSEW)

textoComentarios.config(yscrollcommand=scrollVert.set)

#-------------------------------------------BOTONES_FRAME-------------------------------------------#

botonCreate=Button(miFrame, text="Create", width=20, command=lambda:create())
botonCreate.grid(row=6, column=0, columnspan=4, pady=3)
botonCreate.config(bg="green")

botonRead=Button(miFrame, text="Read", width=20, command=lambda:leer())
botonRead.grid(row=7, column=0, columnspan=4, pady=3)

botonUpdate=Button(miFrame, text="Update", width=20, command=lambda:actualizar())
botonUpdate.grid(row=8, column=0, columnspan=4, pady=3)

botonDelete=Button(miFrame, text="Delete", width=20, command=lambda:delete())
botonDelete.grid(row=9, column=0, columnspan=4, pady=3)
botonDelete.config(bg="red")


try:
    root.mainloop()
    if check_connection():
        print("Cerrando conexión")
        info=messagebox.showinfo("Conexión", "Conexión a BBDD cerrada con éxito")
        miConexion.close()
except:
    root.mainloop()


        