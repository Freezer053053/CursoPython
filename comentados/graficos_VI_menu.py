from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.

root = Tk()  # Crea la ventana principal de la aplicación.

barraMenu = Menu(root)  # Crea una barra de menú en la ventana principal.
root.config(menu=barraMenu, width=300, height=300)  # Configura la ventana principal para que use la barra de menú y establece sus dimensiones.

archivoMenu = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable (sin la línea de separación) dentro de la barra de menú para la opción "Archivo".
archivoMenu.add_command(label="Nuevo")  # Añade un comando al menú "Archivo" con la etiqueta "Nuevo".
archivoMenu.add_command(label="Guardar")  # Añade un comando al menú "Archivo" con la etiqueta "Guardar".
archivoMenu.add_command(label="Guardar como")  # Añade un comando al menú "Archivo" con la etiqueta "Guardar como".
archivoMenu.add_separator()  # Añade una línea separadora en el menú "Archivo".
archivoMenu.add_command(label="Cerrar")  # Añade un comando al menú "Archivo" con la etiqueta "Cerrar".
archivoMenu.add_command(label="Salir")  # Añade un comando al menú "Archivo" con la etiqueta "Salir".

archivoEdicion = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable (sin la línea de separación) dentro de la barra de menú para la opción "Edición".
archivoEdicion.add_command(label="Copiar")  # Añade un comando al menú "Edición" con la etiqueta "Copiar".
archivoEdicion.add_command(label="Cortar")  # Añade un comando al menú "Edición" con la etiqueta "Cortar".
archivoEdicion.add_command(label="Pegar")  # Añade un comando al menú "Edición" con la etiqueta "Pegar".

archivoHerramientas = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable vacío (sin la línea de separación) dentro de la barra de menú para la opción "Herramientas".

archivoAyuda = Menu(barraMenu, tearoff=0)  # Crea un menú desplegable (sin la línea de separación) dentro de la barra de menú para la opción "Ayuda".
archivoAyuda.add_command(label="Licencia")  # Añade un comando al menú "Ayuda" con la etiqueta "Licencia".
archivoAyuda.add_command(label="Acerca de")  # Añade un comando al menú "Ayuda" con la etiqueta "Acerca de".

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)  # Añade el menú "Archivo" a la barra de menú con la etiqueta "Archivo".
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)  # Añade el menú "Edición" a la barra de menú con la etiqueta "Edición".
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)  # Añade el menú "Herramientas" a la barra de menú con la etiqueta "Herramientas".
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)  # Añade el menú "Ayuda" a la barra de menú con la etiqueta "Ayuda".

root.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
