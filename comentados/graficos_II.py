from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.

root = Tk()  # Crea la ventana principal de la aplicación.

miFrame = Frame(root, width="500", height="400")  # Crea un marco (frame) dentro de la ventana principal, con un ancho de 500 píxeles y una altura de 400 píxeles.
miFrame.pack()  # Coloca el marco en la ventana principal (con la configuración predeterminada).

miImagen = PhotoImage(file="graficos/player.png")  # Carga una imagen desde el archivo especificado para ser utilizada en un widget.

# Opciones de configuración de la etiqueta (label) (comentadas):
# miLabel = Label(miFrame, text="Hola!", fg="red", font=("Comic Sans MS", 18))  # Crea una etiqueta con el texto "Hola!", color de fuente rojo y fuente "Comic Sans MS" de tamaño 18.
# miLabel.place(x=250, y=250)  # Coloca la etiqueta en el marco en la posición (250, 250).

# Label(miFrame, text="Hola!").place(x=250, y=250)  # Crea y coloca una etiqueta con el texto "Hola!" en el marco en la posición (250, 250).

miLabel = Label(miFrame, image=miImagen)  # Crea una etiqueta con la imagen cargada previamente.
miLabel.place(x=250, y=250)  # Coloca la etiqueta con la imagen en el marco en la posición (250, 250).

root.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
