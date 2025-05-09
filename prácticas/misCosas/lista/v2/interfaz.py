from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from utils import emergentes
from BBDD import create
from BBDD import createUser
from BBDD import obtener_datos_desde_bd

def avisoLicencia():
    with open(f"prácticas/misCosas/lista/licencia.txt", "r", encoding="utf-8") as archivo:
        licencia = archivo.read()

    messagebox.showinfo("Licencia", licencia)

def ayuda():
    with open(f"prácticas/misCosas/lista/ayuda.txt", "r", encoding="utf-8") as archivo:
        ayuda = archivo.read()

    messagebox.showinfo("Uso de la applicación", ayuda)

#-------------------------------------------VENTANAS_COMPONENTES-------------------------------------------#
def seleccion(opcion):
    match opcion:
        case "Capacitor":
            ventanaCapacitor()
        
        case "Resistencia":
            ventanaResistencias()

        case "Diodo":
            ventanaDiodos()
        
        case "Chip":
            ventanaIC()
        
        case "Transistor":
            ventanaTransistores()


def ventanaCapacitor():
    '''Ventana para introducir los valores de los capacitores'''

    # cargar_propiedades_desde_txt("capacitores.db", "info_capacitores.txt")
    
    def agregar_capacitor():
        datos = {
            "tipo": tipo.get(),
            "polarizado": polarizado.get(),
            "capacitancia": faradios.get(),
            "voltios": voltios.get(),
            "cantidad": cantidad.get()
        }

        if all(datos.values()):  # Validación de que todos los campos estén llenos
            exito = insertar_o_actualizar_componente("capacitores", datos, ["tipo", "polarizado", "capacitancia", "voltios"])
            if exito:
                messagebox.showinfo("Éxito", "Capacitor agregado o actualizado con éxito.")
            else:
                messagebox.showerror("Error", "No se pudo agregar o actualizar el capacitor.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")



    capacitor = Toplevel(root)
    capacitor.title("Capacitores")
    capacitor.geometry('300x300')
    frameCap = Frame(capacitor)
    frameCap.pack()

    labelTipo = Label(frameCap, text="Tipo: ")
    labelTipo.grid(row=0, column=0, padx=5)

    tipos = obtener_datos_desde_bd("capacitores.db", "TIPOS", "TIPO")

    tipo = ttk.Combobox(frameCap,
                    state = "readonly",
                    values = tipos
                    )
    tipo.grid(row=0, column=1, pady=10)
    
    labelPol = Label(frameCap, text="Polarizado: ")
    labelPol.grid(row=1, column=0, padx=5)

    polarizados = obtener_datos_desde_bd("capacitores.db", "POLARIZADOS", "POLARIZADO")

    polarizado = ttk.Combobox(frameCap,
                    state = "readonly",
                    values = polarizados
                    )
    polarizado.grid(row=1, column=1, pady=10)

    labelFar = Label(frameCap, text="Capacitancia (µF): ")
    labelFar.grid(row=2, column=0, padx=5)
    faradios = Entry(frameCap)
    faradios.grid(row=2, column=1, pady=10)

    labelV = Label(frameCap, text="Voltios (V): ")
    labelV.grid(row=3, column=0, padx=5)
    voltios = Entry(frameCap)
    voltios.grid(row=3, column=1, pady=10)

    labelCant = Label(frameCap, text="Cantidad: ")
    labelCant.grid(row=4, column=0, padx=5)
    cantidad = Entry(frameCap, textvariable=cantidad_defecto)
    cantidad.grid(row=4, column=1, pady=10)

    botonAgregar=Button(frameCap, text="Agregar", width=20, command=lambda:agregar_capacitor())
    botonAgregar.grid(row=5, column=0, columnspan=2, pady=3)
#-------------------------------------------CREACION_USUARIOS-------------------------------------------#
def newUser():

    def addUser():
        datos = {
            "nombre": name.get(),
            "ApPaterno": ApP.get(),
            "ApMaterno": ApM.get()
        }

        if all(datos.values()):  # Validación de que todos los campos estén llenos
            exito = createUser("usuarios", datos, ["nombre", "ApPaterno", "ApMaterno"])
            if exito:
                messagebox.showinfo("Éxito", "Usuario agregado con éxito.")
            else:
                messagebox.showerror("Error", "No se pudo agregar el usuario.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    newUser = Toplevel(root)
    newUser.title("Agregar usuarios")
    newUser.geometry('300x200')
    frameUs = Frame(newUser)
    frameUs.pack()

    labelNombre = Label(frameUs, text="Nombre del usuario:")
    labelNombre.grid(row=0, column=0, padx=5)
    name = Entry(frameUs)
    name.grid(row=0, column=1, pady=10)

    labelApP = Label(frameUs, text="Apellido paterno:")
    labelApP.grid(row=1, column=0, padx=5)
    ApP = Entry(frameUs)
    ApP.grid(row=1, column=1, pady=10)

    labelApM = Label(frameUs, text="Apellido materno:")
    labelApM.grid(row=2, column=0, padx=5)
    ApM = Entry(frameUs)
    ApM.grid(row=2, column=1, pady=10)

    botonAceptar=Button(frameUs, text="Aceptar", width=20, command=lambda:addUser())
    botonAceptar.grid(row=3, column=0, columnspan=2, pady=3)

    

#-------------------------------------------VENTANA_PRINCIPAL-------------------------------------------#
root = Tk()
root.title("Gestión de componentes")
#root.resizable(0, 0)
root.geometry('275x150')

create()

miFrameSlct = Frame(root)
miFrameSlct.config(width = 600, height = 400)
miFrameSlct.pack()


#-------------------------------------------MENU_SUPERIOR-------------------------------------------#
barraMenu = Menu(root)
barraMenu.config()
BBDDMenu = Menu(barraMenu, tearoff = 0)
borrarMenu = Menu(barraMenu, tearoff = 0)
CRUDMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu = Menu(barraMenu, tearoff = 0)
root.config(menu = barraMenu, width = 250, height = 400)
            
barraMenu.add_cascade(label = "BBDD", menu = BBDDMenu)
BBDDMenu.add_command(label = "Conectar a BBDD", command = lambda:connect(selectUser.get( )))
BBDDMenu.add_command(label = "Desconectar de BBDD", command = lambda:desconectar())
BBDDMenu.add_separator()
BBDDMenu.add_command(label = "Salir", command = lambda:root.destroy())

# barraMenu.add_cascade(label = "Borrar", menu = borrarMenu)
# borrarMenu.add_command(label = "Borrar campos", command = lambda:borrar())

# barraMenu.add_cascade(label = "CRUD", menu = CRUDMenu)
# CRUDMenu.add_command(label = "Crear", command = lambda:create())
# CRUDMenu.add_command(label = "Leer", command = lambda:leer())
# CRUDMenu.add_command(label = "Actualizar", command = lambda:actualizar())
# CRUDMenu.add_command(label = "Eliminar", command = lambda:delete())

barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)
ayudaMenu.add_command(label = "Licencia", command = lambda:avisoLicencia())
ayudaMenu.add_command(label = "Como usar el programa", command = lambda:ayuda())

#--------------------------opciones-------------------------
usuarios = obtener_datos_desde_bd("BBDD.db", "usuarios", "nombre")

selectUser = ttk.Combobox(miFrameSlct,
                          state = "readonly",
                          values = usuarios
                          )
selectUser.grid(row=0, column=1, pady=5, padx=10, columnspan=3)

labelUser = Label(miFrameSlct, text = "Usuario:")
labelUser.grid(row=0, column=0, sticky="e")

# cargar_propiedades_desde_txt("all_components.db", "componentes.txt")

# componentes = obtener_datos_desde_bd("all_components.db", "TIPOS", "TIPO")

labelSelect = Label(miFrameSlct, text="Componente:")
labelSelect.grid(row=1, column=0, sticky="e")

select = ttk.Combobox(miFrameSlct,
                    state = "readonly",
                    # values = componentes
                    )
select.grid(row=1, column=1, pady=5, padx = 10)



botonView = ttk.Button(miFrameSlct,
                            text="Ver contenido",
                            command = lambda:generar_y_mostrar_txt(selectUser.get())
                        )
botonView.grid(row=2, column=0, pady=5, padx = 10)

botonSelect = ttk.Button(miFrameSlct, text = "Seleccionar", command = lambda:seleccion(select.get()))
botonSelect.grid(row=2, column=1, pady=5, padx = 10)

botonNewUser = ttk.Button(miFrameSlct, text = "Nuevo usuario", command = lambda:newUser())
botonNewUser.grid(row=3, column=0, pady=5, padx = 10)


# connect(selectUser.get())

cantidad_defecto = IntVar()
cantidad_defecto.set("1")

root.mainloop()