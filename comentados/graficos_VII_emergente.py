from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.
from tkinter import messagebox  # Importa el módulo messagebox de tkinter para mostrar cuadros de diálogo.

root = Tk()  # Crea la ventana principal de la aplicación.

def infoAdicional():  # Define una función para mostrar información adicional.
    messagebox.showinfo("Procesador de Álex", "Procesador de textos")  # Muestra un cuadro de información con el título y mensaje especificados.

def avisoLicencia():  # Define una función para mostrar un aviso de licencia.
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")  # Muestra un cuadro de advertencia con el título y mensaje especificados.

def salirApp():  # Define una función para salir de la aplicación.
    # valor = messagebox.askquestion("Salir", "Deseas salir de la aplicación?")  # Pregunta al usuario si desea salir de la aplicación (comentado).

    # if valor == "yes":  # Si el usuario responde "yes"...
    #    root.destroy()  # ...cierra la ventana principal (comentado).

    valor = messagebox.askokcancel("Salir", "Deseas salir de la aplicación?")  # Pregunta al usuario si desea salir de la aplicación con opciones "OK" y "Cancelar".

    if valor == True:  # Si el usuario responde "OK" (True)...
        root.destroy()  # ...cierra la ventana principal.

def cerrarDoc():  # Define una función para intentar cerrar un documento.
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento, documento bloqueado")  # Pregunta al usuario si desea reintentar cerrar el documento con opciones "Reintentar" y "Cancelar".

    if valor == True:  # Si el usuario responde "Reintentar" (True)...
        cerrarDoc()  # ...vuelve a intentar cerrar el documento llamando a la misma función.
    if valor == False:  # Si el usuario responde "Cancelar" (False)...
        root.destroy()  # ...cierra la ventana principal.

barraMenu = Menu(root)  # Crea una barra de menú en la ventana principal.
root.config(menu=barraMenu, width=300, height=300)  # Configura la ventana principal para que use la barra de menú y establece sus dimensiones.

archivoMenu = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable (sin la línea de separación) dentro de la barra de menú para la opción "Archivo".
archivoMenu.add_command(label="Nuevo")  # Añade un comando al menú "Archivo" con la etiqueta "Nuevo".
archivoMenu.add_command(label="Guardar")  # Añade un comando al menú "Archivo" con la etiqueta "Guardar".
archivoMenu.add_command(label="Guardar como")  # Añade un comando al menú "Archivo" con la etiqueta "Guardar como".
archivoMenu.add_separator()  # Añade una línea separadora en el menú "Archivo".
archivoMenu.add_command(label="Cerrar", command=cerrarDoc)  # Añade un comando al menú "Archivo" con la etiqueta "Cerrar" que llama a la función cerrarDoc.
archivoMenu.add_command(label="Salir", command=salirApp)  # Añade un comando al menú "Archivo" con la etiqueta "Salir" que llama a la función salirApp.

archivoEdicion = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable (sin la línea de separación) dentro de la barra de menú para la opción "Edición".
archivoEdicion.add_command(label="Copiar")  # Añade un comando al menú "Edición" con la etiqueta "Copiar".
archivoEdicion.add_command(label="Cortar")  # Añade un comando al menú "Edición" con la etiqueta "Cortar".
archivoEdicion.add_command(label="Pegar")  # Añade un comando al menú "Edición" con la etiqueta "Pegar".

archivoHerramientas = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable vacío (sin la línea de separación) dentro de la barra de menú para la opción "Herramientas".

archivoAyuda = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable (sin la línea de separación) dentro de la barra de menú para la opción "Ayuda".
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)  # Añade un comando al menú "Ayuda" con la etiqueta "Licencia" que llama a la función avisoLicencia.
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)  # Añade un comando al menú "Ayuda" con la etiqueta "Acerca de..." que llama a la función infoAdicional.

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)  # Añade el menú "Archivo" a la barra de menú con la etiqueta "Archivo".
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)  # Añade el menú "Edición" a la barra de menú con la etiqueta "Edición".
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)  # Añade el menú "Herramientas" a la barra de menú con la etiqueta "Herramientas".
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)  # Añade el menú "Ayuda" a la barra de menú con la etiqueta "Ayuda".

root.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
