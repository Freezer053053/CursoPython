from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.

raiz = Tk()  # Crea la ventana principal de la aplicación.

raiz.title("Ventana")  # Establece el título de la ventana principal.

raiz.resizable(1, 1)  # Permite redimensionar la ventana en ambas direcciones (ancho y alto).

raiz.iconbitmap("graficos/icono.ico")  # Establece el icono de la ventana principal con el archivo indicado.

# raiz.geometry("800x600")  # Define el tamaño de la ventana principal (comentado).

raiz.config(bg="blue")  # Configura el color de fondo de la ventana principal a azul.
raiz.config(bd="35")  # Configura el borde de la ventana principal con un ancho de 35 píxeles.
raiz.config(relief="groove")  # Establece el estilo del borde de la ventana principal como "groove" (acanalado).

miFrame = Frame()  # Crea un marco (frame) que se puede utilizar para agrupar otros widgets.

# Opciones de configuración del empaquetado del marco (comentadas):
# miFrame.pack(side="right", anchor="n")  # Coloca el marco en el lado derecho y lo ancla al norte.
# miFrame.pack(fill="x")  # Permite que el marco se expanda solo en el eje x (ancho).
# miFrame.pack(fill="y", expand="True")  # Permite que el marco se expanda solo en el eje y (alto) y ocupa todo el espacio disponible.
# miFrame.pack(fill="both", expand="True")  # Permite que el marco se expanda tanto en el eje x como en el eje y y ocupe todo el espacio disponible.
miFrame.pack()  # Coloca el marco en la ventana principal (con la configuración predeterminada).

miFrame.config(bg="blue")  # Configura el color de fondo del marco a azul.

miFrame.config(width="650", height="350")  # Establece el tamaño del marco a 650 píxeles de ancho y 350 píxeles de alto.

miFrame.config(bd="35")  # Configura el borde del marco con un ancho de 35 píxeles.
miFrame.config(relief="sunken")  # Establece el estilo del borde del marco como "sunken" (hundido).
miFrame.config(cursor="hand2")  # Cambia el cursor a una mano cuando se pasa sobre el marco.

raiz.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
