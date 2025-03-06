from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.

root = Tk()  # Crea la ventana principal de la aplicación.

miFrame = Frame(root, width="500", height="400")  # Crea un marco (frame) dentro de la ventana principal, con un ancho de 500 píxeles y una altura de 400 píxeles.
miFrame.pack()  # Coloca el marco en la ventana principal (con la configuración predeterminada).
# miFrame.pack(side=LEFT, anchor=N)  # Coloca el marco en el lado izquierdo de la ventana y lo ancla al norte (comentado).

minombre = StringVar()  # Declara una variable de tipo StringVar para almacenar texto.

# ---------------------------------------------------------#
cuadroNombre = Entry(miFrame, textvariable=minombre)  # Crea un campo de entrada (Entry) vinculado a la variable minombre.
cuadroNombre.grid(row=0, column=1, pady=5, padx=10)  # Coloca el campo de entrada en la posición (0, 1) de la rejilla del marco con espacio alrededor.
cuadroNombre.config(justify="center")  # Configura el texto del campo de entrada para que esté centrado.

nombreLabel = Label(miFrame, text="Nombre: ")  # Crea una etiqueta con el texto "Nombre:".
nombreLabel.grid(row=0, column=0, sticky="e")  # Coloca la etiqueta en la posición (0, 0) de la rejilla del marco y la alinea a la derecha (este).
# ---------------------------------------------------------#
cuadroApellido = Entry(miFrame)  # Crea un campo de entrada para el apellido.
cuadroApellido.grid(row=1, column=1, pady=5, padx=10)  # Coloca el campo de entrada en la posición (1, 1) de la rejilla del marco con espacio alrededor.
cuadroApellido.config(justify="center")  # Configura el texto del campo de entrada para que esté centrado.

apellidoLabel = Label(miFrame, text="Apellido: ")  # Crea una etiqueta con el texto "Apellido:".
apellidoLabel.grid(row=1, column=0, sticky="e")  # Coloca la etiqueta en la posición (1, 0) de la rejilla del marco y la alinea a la derecha (este).
# ---------------------------------------------------------#
cuadroDireccion = Entry(miFrame)  # Crea un campo de entrada para la dirección.
cuadroDireccion.grid(row=2, column=1, pady=5, padx=10)  # Coloca el campo de entrada en la posición (2, 1) de la rejilla del marco con espacio alrededor.
cuadroDireccion.config(justify="center")  # Configura el texto del campo de entrada para que esté centrado.

direccionLabel = Label(miFrame, text="Dirección de casa: ")  # Crea una etiqueta con el texto "Dirección de casa:".
direccionLabel.grid(row=2, column=0, sticky="e")  # Coloca la etiqueta en la posición (2, 0) de la rejilla del marco y la alinea a la derecha (este).
# ---------------------------------------------------------#
cuadroContraseña = Entry(miFrame)  # Crea un campo de entrada para la contraseña.
cuadroContraseña.grid(row=3, column=1, pady=5, padx=10)  # Coloca el campo de entrada en la posición (3, 1) de la rejilla del marco con espacio alrededor.
cuadroContraseña.config(justify="center", show="*")  # Configura el texto del campo de entrada para que esté centrado y muestra asteriscos en lugar de la contraseña real.

contraseñaLabel = Label(miFrame, text="Contraseña: ")  # Crea una etiqueta con el texto "Contraseña:".
contraseñaLabel.grid(row=3, column=0, sticky="e")  # Coloca la etiqueta en la posición (3, 0) de la rejilla del marco y la alinea a la derecha (este).
# ---------------------------------------------------------#
textoComentarios = Text(miFrame, width=16, height=5)  # Crea un campo de texto grande para comentarios, con un ancho de 16 caracteres y una altura de 5 líneas.
textoComentarios.grid(row=4, column=1, pady=5, padx=10)  # Coloca el campo de texto en la posición (4, 1) de la rejilla del marco con espacio alrededor.

comentariosLabel = Label(miFrame, text="Comentarios: ")  # Crea una etiqueta con el texto "Comentarios:".
comentariosLabel.grid(row=4, column=0, sticky="e")  # Coloca la etiqueta en la posición (4, 0) de la rejilla del marco y la alinea a la derecha (este).

scrollVert = Scrollbar(miFrame, command=textoComentarios.yview)  # Crea una barra de desplazamiento vertical para el campo de texto y la vincula a su vista vertical.
scrollVert.grid(row=4, column=2, sticky=NSEW)  # Coloca la barra de desplazamiento en la posición (4, 2) de la rejilla del marco y la hace extensible en todas las direcciones.

textoComentarios.config(yscrollcommand=scrollVert.set)  # Configura el campo de texto para que la barra de desplazamiento se mueva al desplazarse por el texto.
# ---------------------------------------------------------#
 
def codigoBoton():  # Define una función para el botón.
    minombre.set("Álex")  # Establece el valor del campo de entrada "Nombre" a "Álex" cuando se presiona el botón.

botonEnvio = Button(root, text="Enviar", command=codigoBoton)  # Crea un botón con el texto "Enviar" que llama a la función cuando se presiona.
botonEnvio.pack()  # Coloca el botón en la ventana principal (con la configuración predeterminada).

root.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
