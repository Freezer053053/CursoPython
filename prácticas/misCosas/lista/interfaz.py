from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from utils import emergentes
from BBDD import *
from BBDD import insertar_o_actualizar_componente


# def graficos():

def generar_txt():
    from BBDD import contenido  # Importamos la función de la BBDD
    componentes = contenido()
    
    if componentes:
        try:
            with open("lista_componentes.txt", "w", encoding="utf-8") as archivo:
                archivo.write("Lista de Componentes:\n\n")
                
                for tabla, datos in componentes.items():
                    archivo.write(f"Tabla: {tabla.capitalize()}\n")
                    for componente in datos:
                        archivo.write(f"{componente}\n")
                    archivo.write("\n")
            
            messagebox.showinfo("Éxito", "Archivo 'lista_componentes.txt' creado con éxito.")
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
    tipo = ttk.Combobox(frameTr,
                    state = "readonly",
                    values = [
                        "Mosfet",
                        "Transistor"
                        ]
                    )
    
    tipo.grid(row=0, column=1, pady=10)

    labelPat = Label(frameTr, text="Patillage: ")
    labelPat.grid(row=1, column=0, padx=5)
    patillage = ttk.Combobox(frameTr,
                    state = "readonly",
                    values = [
                        "NPN",
                        "PNP"
                        ]
                    )
    patillage.grid(row=1, column=1, pady=10)

    labelEnc = Label(frameTr, text="Encapsulado: ")
    labelEnc.grid(row=2, column=0, padx=5)
    encapsulado = ttk.Combobox(frameTr,
                    state = "readonly",
                    values = [
                        "TO-92",
                        "TO-5",
                        "TO-220",
                        "TO-3",
                        "SOT-23",
                        "TO-258"
                        ]
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
    marca = ttk.Combobox(frameIC,
                    state = "readonly",
                    values = [
                        "Aeroflex",
                        "Agere Systems",
                        "Achronix Semiconductor",
                        "Allegro MicroSystems",
                        "Altera (ahora parte de Intel)",
                        "AMD (Advanced Micro Devices)",
                        "Ambarella",
                        "Amkor Technology",
                        "Analog Devices",
                        "Applied Materials",
                        "ARM Holdings",
                        "ASE Group (Advanced Semiconductor Engineering)",
                        "ASML",
                        "ASPEED Technology",
                        "Avago Technologies (fusionada con Broadcom)",
                        "Broadcom",
                        "Broadcom Corporation",
                        "Cadence Design Systems",
                        "Cirrus Logic",
                        "Conexant Systems",
                        "Cypress Semiconductor",
                        "Dialog Semiconductor",
                        "Etron Technology",
                        "Everspin Technologies",
                        "Fairchild Semiconductor (ahora parte de ON Semiconductor)",
                        "Freescale Semiconductor (fusionada con NXP)",
                        "Fujitsu",
                        "GlobalFoundries",
                        "Hitachi",
                        "IBM",
                        "IC Insights",
                        "IDT (Integrated Device Technology, adquirida por Renesas)",
                        "Imagination Technologies",
                        "Infineon Technologies",
                        "Intersil (adquirida por Renesas)",
                        "Intel Corporation",
                        "ISSI (Integrated Silicon Solution Inc.)",
                        "Lite-On",
                        "Lattice Semiconductor",
                        "Macronix",
                        "Macronix International",
                        "Marvell Technology",
                        "Maxim Integrated",
                        "Maxim Integrated Circuits",
                        "MediaTek",
                        "Melexis",
                        "Microchip Technology",
                        "Micron Technology",
                        "Microsemi Corporation",
                        "Mitsubishi Electric",
                        "National Semiconductor (adquirida por Texas Instruments)",
                        "NVIDIA",
                        "Nexperia",
                        "NXP Semiconductors",
                        "Omnivision Technologies",
                        "ON Semiconductor",
                        "Panasonic",
                        "Pericom Semiconductor",
                        "PixArt Imaging",
                        "PLX Technology",
                        "PMC-Sierra (ahora parte de Microsemi)",
                        "Power Integrations",
                        "Qorvo",
                        "Qualcomm",
                        "Realtek Semiconductor",
                        "Renesas Electronics",
                        "Renesas SP Drivers",
                        "ROHM Group",
                        "Rohm Semiconductor",
                        "Samsung Electronics",
                        "Seiko Epson",
                        "Semtech",
                        "SiTime",
                        "Silicon Labs",
                        "Silicon Motion",
                        "SK Hynix",
                        "SMIC (Semiconductor Manufacturing International Corporation)",
                        "Sony Semiconductor",
                        "Spreadtrum (ahora parte de UNISOC)",
                        "STMicroelectronics",
                        "Synopsys",
                        "Texas Instruments",
                        "Toshiba",
                        "Tower Semiconductor",
                        "Transphorm",
                        "Triquint Semiconductor (fusionada con RF Micro Devices para formar Qorvo)",
                        "Trident Microsystems",
                        "TSMC (Taiwan Semiconductor Manufacturing Company)",
                        "UMC (United Microelectronics Corporation)",
                        "UNISOC",
                        "Vishay Intertechnology",
                        "Winbond Electronics",
                        "Wolfspeed (antes parte de Cree Inc.)",
                        "Xilinx",
                        "Zilog"
                        ]
                    )
    marca.grid(row=0, column=1, pady=10)

    labelTipo = Label(frameIC, text="Tipo: ")
    labelTipo.grid(row=1, column=0, padx=5)
    tipo = ttk.Combobox(frameIC,
                    state = "readonly",
                    values = [
                        "ROM",
                        "Microprocessor",
                        "CMOS",
                        "EEPROM",
                        "Flash Memory",
                        "Static RAM",
                        "TTL",
                        "ECL",
                        "MOS",
                        "I2L"
                        ]
                    )
    tipo.grid(row=1, column=1, pady=10)
    
    labelEncapsulado = Label(frameIC, text="Encapsulado: ")
    labelEncapsulado.grid(row=2, column=0, padx=5)
    encapsulado = ttk.Combobox(frameIC,
                    state = "readonly",
                    values = [
                        "DIP",
                        "PGA",
                        "SOP",
                        "TSOP",
                        "QFP",
                        "SOJ",
                        "QFJ",
                        "QFN",
                        "TCP",
                        "BGA",
                        "LGA"
                        ]
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
            "color": color.get() if tipo.get() not in ["Zener", "Zener SMD"] else None,
            "voltios": voltage.get(),
            "cantidad": cantidad.get()
        }

        # Validar que los campos obligatorios estén completos
        datos_requeridos = {key: value for key, value in datos.items() if value is not None}
        if all(value != "" for value in datos_requeridos.values()):  # Validación
            # Claves relevantes dependiendo del tipo de diodo
            columnas_clave = ["tipo", "voltios"]
            if tipo.get() not in ["Zener", "Zener SMD"]:
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
    
    def tipo_seleccionado(event):
        if tipo.get() in ["Zener", "Zener SMD"]:
            color.config(state="disabled")
        else:
            color.config(state="readonly")
    
    tipo = ttk.Combobox(frameDi,
                        state="readonly",
                        values=["Zener", "Zener SMD", "LED", "LED SMD"])
    tipo.grid(row=0, column=1, pady=10)
    tipo.bind("<<ComboboxSelected>>", tipo_seleccionado)

    labelColor = Label(frameDi, text="Color: ")
    labelColor.grid(row=1, column=0, padx=5)
    color = ttk.Combobox(frameDi,
                        state="readonly",
                        values=[
                            "Rojo",
                            "Verde",
                            "Azul",
                            "Amarillo",
                            "Naranja",
                            "Morado",
                            "Blanco",
                            "Infrarrojo"
                        ])
    color.grid(row=1, column=1, pady=10)

    labelVol = Label(frameDi, text="Voltage (V): ")
    labelVol.grid(row=2, column=0, padx=5)
    voltage = Entry(frameDi)
    voltage.grid(row=2, column=1, pady=10)

    labelCant = Label(frameDi, text="Cantidad: ")
    labelCant.grid(row=3, column=0, padx=5)
    cantidad = Entry(frameDi, textvariable=cantidad_defecto)
    cantidad.grid(row=3, column=1, pady=10)

    botonAgregar=Button(frameDi, text="Agregar", width=20, command=lambda:agregar_diodo())
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

    labelTipo = Label(frameRes, text="Tipo: ")
    labelTipo.grid(row=0, column=0, padx=5)
    tipo = ttk.Combobox(frameRes,
                    state = "readonly",
                    values = [
                        "Fija", "Fija SMD", "Variable", "Fotorresistencia", "Fotorresistencia SMD", "Termorresistencia", "Termorresistencia SMD"
                        ]
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
    tipo = ttk.Combobox(frameCap,
                    state = "readonly",
                    values = [
                        "Electrolítico","Electrolítico SMD", "Cerámico", "Cerámico SMD", "Film", "Mica", "Variable"
                        ]
                    )
    tipo.grid(row=0, column=1, pady=10)
    
    labelPol = Label(frameCap, text="Polarizado: ")
    labelPol.grid(row=1, column=0, padx=5)
    polarizado = ttk.Combobox(frameCap,
                    state = "readonly",
                    values = ["Si", "No"]
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
root.geometry('224x100')

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
BBDDMenu.add_command(label = "Conectar a BBDD", command = lambda:connect())
BBDDMenu.add_command(label = "Desconectar de BBDD", command = lambda:desconectar())
BBDDMenu.add_separator()
BBDDMenu.add_command(label = "Salir", command = lambda:salir())

barraMenu.add_cascade(label = "Borrar", menu = borrarMenu)
borrarMenu.add_command(label = "Borrar campos", command = lambda:borrar())

barraMenu.add_cascade(label = "CRUD", menu = CRUDMenu)
CRUDMenu.add_command(label = "Crear", command = lambda:create())
CRUDMenu.add_command(label = "Leer", command = lambda:leer())
CRUDMenu.add_command(label = "Actualizar", command = lambda:actualizar())
CRUDMenu.add_command(label = "Eliminar", command = lambda:delete())

barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)
ayudaMenu.add_command(label = "Licencia", command = lambda:avisoLicencia())
ayudaMenu.add_command(label = "Como usar el programa", command = lambda:ayuda())

#--------------------------opciones-------------------------

select = ttk.Combobox(miFrameSlct,
                    state = "readonly",
                    values = ["Capacitor", "Diodo", "Resistencia", "Chip", "Transistores"]
                    )
select.grid(row=0, column=0, pady=5, padx = 10)



botonSelect = ttk.Button(miFrameSlct, text = "Seleccionar", command = lambda:seleccion(select.get()))
botonSelect.grid(row=1, column=0, pady=5, padx = 10)

botonView = ttk.Button(miFrameSlct, text = "Ver contenido", command = lambda:generar_txt())
botonView.grid(row=2, column=0, pady=5, padx = 10)

connect()

cantidad_defecto = IntVar()
cantidad_defecto.set("1")

root.mainloop()