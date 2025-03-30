from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from utils import emergentes
from BBDD import *
from BBDD import insertar_o_actualizar_componente
from fingerprints import cargar_propiedades_desde_txt
from fingerprints import obtener_datos_desde_bd



# def graficos():

def ayuda():
    with open(f"prácticas/misCosas/lista/ayuda.txt", "r", encoding="utf-8") as archivo:
        ayuda = archivo.read()

    messagebox.showinfo("Uso de la applicación", ayuda)

def generar_y_mostrar_txt(user):
    from BBDD import contenido  # Importamos la función de la BBDD
    componentes = contenido()
    
    if componentes:
        try:
            with open(f"lista_componentes_{user}.txt", "w", encoding="utf-8") as archivo:
                archivo.write("Lista de Componentes:\n\n")
                
                for tabla, datos in componentes.items():
                    archivo.write(f"Tabla: {tabla.capitalize()}\n")
                    for componente in datos:
                        archivo.write(f"{componente}\n")
                    archivo.write("\n")
            
            with open(f"lista_componentes.txt", "r", encoding="utf-8") as archivo:
                lista = archivo.read()

            messagebox.showinfo("Éxito", "Archivo 'lista_componentes.txt' creado con éxito.")
            messagebox.showinfo("Componentes", lista)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el archivo: {e}")
    else:
        messagebox.showwarning("Advertencia", "No hay componentes registrados en la base de datos.")


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
        
        case "Transistores":
            ventanaTransistores()

def ventanaTransistores():

    cargar_propiedades_desde_txt("transistores.db", "info_transistores.txt")
    

    def agregar_transistor():
        datos = {
            "tipo": tipo.get(),
            "patillage": patillage.get(),
            "encapsulado": encapsulado.get(),
            "modelo": modelo.get(),
            "cantidad": cantidad.get()
        }
        if all(datos.values()):  # Validación de que todos los campos estén llenos
            exito = insertar_o_actualizar_componente("transistores", datos, ["tipo", "patillage", "encapsulado", "modelo"])
            if exito:
                messagebox.showinfo("Éxito", "Transistor agregado o actualizado con éxito.")
            else:
                messagebox.showerror("Error", "No se pudo agregar o actualizar el transistor.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")


    transistor = Toplevel(root)
    transistor.title("Transistores")
    transistor.geometry("300x400")
    frameTr = Frame(transistor)
    frameTr.pack()

    labelTipo = Label(frameTr, text="Tipo: ")
    labelTipo.grid(row=0, column=0, padx=5)

    tipos = obtener_datos_desde_bd("transistores.db", "TIPOS", "TIPO")

    tipo = ttk.Combobox(frameTr,
                    state = "readonly",
                    values = tipos
                    )
    
    tipo.grid(row=0, column=1, pady=10)

    labelPat = Label(frameTr, text="Encapsulado: ")
    labelPat.grid(row=1, column=0, padx=5)

    patillages = obtener_datos_desde_bd("transistores.db", "PATILLAGES", "PATILLAGE")

    patillage = ttk.Combobox(frameTr,
                    state = "readonly",
                    values = patillages
                    )
    patillage.grid(row=1, column=1, pady=10)

    labelEnc = Label(frameTr, text="Patillage: ")
    labelEnc.grid(row=2, column=0, padx=5)

    encapsulados = obtener_datos_desde_bd("transistores.db", "ENCAPSULADOS", "ENCAPSULADO")

    encapsulado = ttk.Combobox(frameTr,
                    state = "readonly",
                    values = encapsulados
                    )
    encapsulado.grid(row=2, column=1, pady=10)

    labelModelo = Label(frameTr, text="Modelo: ")
    labelModelo.grid(row=3, column=0, padx=5)
    modelo = Entry(frameTr)
    modelo.grid(row=3, column=1, pady=10)

    labelCant = Label(frameTr, text="Cantidad: ")
    labelCant.grid(row=4, column=0, padx=5)
    cantidad = Entry(frameTr, textvariable=cantidad_defecto)
    cantidad.grid(row=4, column=1, pady=10)

    botonAgregar=Button(frameTr, text="Agregar", width=20, command=lambda:agregar_transistor())
    botonAgregar.grid(row=5, column=0, columnspan=2, pady=3)
    

    

def ventanaIC():
    cargar_propiedades_desde_txt("chips.db", "info_chips.txt")

    def agregar_ic():
        datos = {
            "marca": marca.get(),
            "tipo": tipo.get(),
            "encapsulado": encapsulado.get(),
            "modelo": modelo.get(),
            "cantidad": cantidad.get()
        }

        if all(datos.values()):  # Validación de que todos los campos estén llenos
            exito = insertar_o_actualizar_componente("Chips", datos, ["marca", "tipo", "encapsulado", "modelo"])
            if exito:
                messagebox.showinfo("Éxito", "Circuito integrado agregado o actualizado con éxito.")
            else:
                messagebox.showerror("Error", "No se pudo agregar o actualizar el circuito integrado.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")



    ic = Toplevel(root)
    ic.title("Circuitos integrados")
    ic.geometry("300x400")
    frameIC = Frame(ic)
    frameIC.pack()

    labelMarca = Label(frameIC, text="Marca: ")
    labelMarca.grid(row=0, column=0, padx=5)


    marcas = obtener_datos_desde_bd("chips.db", "MARCAS", "MARCA")

    marca = ttk.Combobox(frameIC,
                    state = "readonly",
                    values = marcas
                    )
    marca.grid(row=0, column=1, pady=10)

    labelTipo = Label(frameIC, text="Tipo: ")
    labelTipo.grid(row=1, column=0, padx=5)

    tipos = obtener_datos_desde_bd("chips.db", "TIPOS", "TIPO")

    tipo = ttk.Combobox(frameIC,
                    state = "readonly",
                    values = tipos
                    )
    tipo.grid(row=1, column=1, pady=10)
    
    labelEncapsulado = Label(frameIC, text="Encapsulado: ")
    labelEncapsulado.grid(row=2, column=0, padx=5)

    encapsulados = obtener_datos_desde_bd("chips.db", "ENCAPSULADOS", "ENCAPSULADO")

    encapsulado = ttk.Combobox(frameIC,
                    state = "readonly",
                    values = encapsulados
                    )
    encapsulado.grid(row=2, column=1, pady=10)

    labelModelo = Label(frameIC, text="Modelo: ")
    labelModelo.grid(row=3, column=0, padx=5)
    modelo = Entry(frameIC)
    modelo.grid(row=3, column=1, pady=10)

    labelCant = Label(frameIC, text="Cantidad: ")
    labelCant.grid(row=4, column=0, padx=5)
    cantidad = Entry(frameIC, textvariable=cantidad_defecto)
    cantidad.grid(row=4, column=1, pady=10)

    botonAgregar=Button(frameIC, text="Agregar", width=20, command=lambda:agregar_ic())
    botonAgregar.grid(row=5, column=0, columnspan=2, pady=3)
    

def ventanaDiodos():
    def agregar_diodo():
        datos = {
            "tipo": tipo.get(),
            "color": color.get() if tipo.get() not in tipos_requieren_desactivacion else None,
            "voltios": voltage.get(),
            "cantidad": cantidad.get()
        }

        # Validar que los campos obligatorios estén completos
        datos_requeridos = {key: value for key, value in datos.items() if value is not None}
        if all(value != "" for value in datos_requeridos.values()):  # Validación
            # Claves relevantes dependiendo del tipo de diodo
            columnas_clave = ["tipo", "voltios"]
            if tipo.get() not in tipos_requieren_desactivacion:
                columnas_clave.append("color")

            exito = insertar_o_actualizar_componente("diodos", datos, columnas_clave)
            if exito:
                messagebox.showinfo("Éxito", "Diodo agregado o actualizado con éxito.")
            else:
                messagebox.showerror("Error", "No se pudo agregar o actualizar el diodo.")
        else:
            messagebox.showerror("Error", "Todos los campos obligatorios deben ser rellenados.")

    diodos = Toplevel(root)
    diodos.title("Diodos")
    diodos.geometry("300x200")
    frameDi = Frame(diodos)
    frameDi.pack()

    labelTipo = Label(frameDi, text="Tipo: ")
    labelTipo.grid(row=0, column=0, padx=5)

    # Cargar tipos y colores desde la base de datos
    cargar_propiedades_desde_txt("diodos.db", "info_diodos.txt")
    tipos = obtener_datos_desde_bd("diodos.db", "TIPOS", "TIPO")
    tipos_sin_colores = obtener_datos_desde_bd("diodos.db", "TIPOS_SIN_COLORES", "TIPO")
    colores = obtener_datos_desde_bd("diodos.db", "COLORES", "COLOR")

    # Subconjunto de tipos que desactivan el color
    tipos_requieren_desactivacion = tipos_sin_colores

    def tipo_seleccionado(event):
        if tipo.get() in tipos_requieren_desactivacion:
            # Desactivar la combobox de color para los tipos específicos
            color.set("")  # Limpiar selección de color
            color.config(state="disabled")
        else:
            # Reactivar la combobox de color para otros tipos
            color.config(state="readonly")

    tipo = ttk.Combobox(frameDi,
                        state="readonly",
                        values = tipos_sin_colores + tipos)
    tipo.grid(row=0, column=1, pady=10)
    tipo.bind("<<ComboboxSelected>>", tipo_seleccionado)

    labelColor = Label(frameDi, text="Color: ")
    labelColor.grid(row=1, column=0, padx=5)
    color = ttk.Combobox(frameDi, state="readonly", values = colores)
    color.grid(row=1, column=1, pady=10)

    labelVol = Label(frameDi, text="Voltage (V): ")
    labelVol.grid(row=2, column=0, padx=5)
    voltage = Entry(frameDi)
    voltage.grid(row=2, column=1, pady=10)

    labelCant = Label(frameDi, text="Cantidad: ")
    labelCant.grid(row=3, column=0, padx=5)
    cantidad = Entry(frameDi, textvariable=cantidad_defecto)
    cantidad.grid(row=3, column=1, pady=10)

    botonAgregar = Button(frameDi, text="Agregar", width=20, command=lambda: agregar_diodo())
    botonAgregar.grid(row=4, column=0, columnspan=2, pady=3)


    
    # view = color.view()

    # while (tipo.get() == "Zener" or tipo.get() == "Zener SMD" or tipo.get() == ""):
    #     view.setHiden(True)
    
def ventanaResistencias():

    def agregar_resistencia():
        datos = {
            "tipo": tipo.get(),
            "valor": ohmios.get(),
            "cantidad": cantidad.get()
        }

        if all(datos.values()):  # Validación de que todos los campos estén llenos
            exito = insertar_o_actualizar_componente("resistencias", datos, ["tipo", "valor"])
            if exito:
                messagebox.showinfo("Éxito", "Resistencia agregada o actualizada con éxito.")
            else:
                messagebox.showerror("Error", "No se pudo agregar o actualizar la resistencia.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")



    resistencia = Toplevel(root)
    resistencia.title("Resistencias")
    resistencia.geometry("300x200")
    frameRes = Frame(resistencia)
    frameRes.pack()

    cargar_propiedades_desde_txt("resistencias.db", "info_resistencias.txt")
    tipos = obtener_datos_desde_bd("resistencias.db", "TIPOS", "TIPO")

    labelTipo = Label(frameRes, text="Tipo: ")
    labelTipo.grid(row=0, column=0, padx=5)
    tipo = ttk.Combobox(frameRes,
                    state = "readonly",
                    values = tipos
                    )
    tipo.grid(row=0, column=1, pady=10)

    labelValor = Label(frameRes, text="Valor (kΩ): ")
    labelValor.grid(row=1, column=0, padx=5)
    ohmios = Entry(frameRes)
    ohmios.grid(row=1, column=1, pady=10)

    labelCant = Label(frameRes, text="Cantidad: ")
    labelCant.grid(row=2, column=0, padx=5)
    cantidad = Entry(frameRes, textvariable=cantidad_defecto)
    cantidad.grid(row=2, column=1, pady=10)

    botonAgregar=Button(frameRes, text="Agregar", width=20, command=lambda:agregar_resistencia())
    botonAgregar.grid(row=3, column=0, columnspan=2, pady=3)




def ventanaCapacitor():
    '''Ventana para introducir los valores de los capacitores'''

    cargar_propiedades_desde_txt("capacitores.db", "info_capacitores.txt")
    
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
    

# def ventana():
#     '''Crea la ventana principal del programa.
#     No requiere parámetros'''

root = Tk()
root.title("Gestión de componentes")
#root.resizable(0, 0)
root.geometry('275x150')

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
selectUser = ttk.Combobox(miFrameSlct,
                          state = "readonly",
                          values = ["alex", "jorge"]
                          )
selectUser.grid(row=0, column=1, pady=5, padx=10, columnspan=3)

labelUser = Label(miFrameSlct, text = "Usuario:")
labelUser.grid(row=0, column=0, sticky="e")

cargar_propiedades_desde_txt("all_components.db", "componentes.txt")

componentes = obtener_datos_desde_bd("all_components.db", "TIPOS", "TIPO")

labelSelect = Label(miFrameSlct, text="Componente:")
labelSelect.grid(row=1, column=0, sticky="e")

select = ttk.Combobox(miFrameSlct,
                    state = "readonly",
                    values = componentes
                    )
select.grid(row=1, column=1, pady=5, padx = 10)



botonView = ttk.Button(miFrameSlct,
                            text="Ver contenido",
                            command = lambda:generar_y_mostrar_txt(selectUser.get())
                        )
botonView.grid(row=2, column=0, pady=5, padx = 10)

botonSelect = ttk.Button(miFrameSlct, text = "Seleccionar", command = lambda:seleccion(select.get()))
botonSelect.grid(row=2, column=1, pady=5, padx = 10)

botonNewUser = ttk.Button(miFrameSlct, text = "Nuevo usuario", command = lambda:crear_usuario())
botonNewUser.grid(row=3, column=0, pady=5, padx = 10)


connect(selectUser.get())

cantidad_defecto = IntVar()
cantidad_defecto.set("1")

root.mainloop()