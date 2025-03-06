from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.

root = Tk()  # Crea la ventana principal de la aplicación.
root.title("CheckButtons")  # Establece el título de la ventana principal a "CheckButtons".

playa = IntVar()  # Declara una variable de tipo IntVar para almacenar enteros, utilizada para el checkbutton "playa".
montagna = IntVar()  # Declara una variable de tipo IntVar para almacenar enteros, utilizada para el checkbutton "montaña".
turismo = IntVar()  # Declara una variable de tipo IntVar para almacenar enteros, utilizada para el checkbutton "turismo".

def opciones():  # Define una función que se ejecuta cuando se selecciona un checkbutton.
    opcionEscogida = ""  # Inicializa una cadena vacía para almacenar las opciones escogidas.

    if playa.get() == 1:  # Si el valor de "playa" es 1 (checkbutton seleccionado)...
        opcionEscogida += " playa"  # ...añade "playa" a la cadena de opciones escogidas.

    if montagna.get() == 1:  # Si el valor de "montaña" es 1 (checkbutton seleccionado)...
        opcionEscogida += " montaña"  # ...añade "montaña" a la cadena de opciones escogidas.

    if turismo.get() == 1:  # Si el valor de "turismo" es 1 (checkbutton seleccionado)...
        opcionEscogida += " turismo"  # ...añade "turismo" a la cadena de opciones escogidas.

    textoFinal.config(text=opcionEscogida)  # Actualiza el texto del Label "textoFinal" con las opciones escogidas.

foto = PhotoImage(file="graficos/avion.png")  # Carga una imagen desde el archivo especificado para ser utilizada en un widget.
Label(root, image=foto).pack()  # Crea y empaqueta una etiqueta con la imagen cargada en la ventana principal.
frame = Frame(root)  # Crea un marco (frame) dentro de la ventana principal.
frame.pack()  # Coloca el marco en la ventana principal (con la configuración predeterminada).

Label(frame, text="Elige destinos", width=50).pack()  # Crea y empaqueta una etiqueta con el texto "Elige destinos" en el marco, con un ancho de 50 caracteres.

Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=opciones).pack()  # Crea y empaqueta un checkbutton con el texto "playa", vinculado a la variable "playa", con valor 1 al ser seleccionado y que llama a la función "opciones" cuando se selecciona.
Checkbutton(frame, text="montaña", variable=montagna, onvalue=1, offvalue=0, command=opciones).pack()  # Crea y empaqueta un checkbutton con el texto "montaña", vinculado a la variable "montaña", con valor 1 al ser seleccionado y que llama a la función "opciones" cuando se selecciona.
Checkbutton(frame, text="turismo", variable=turismo, onvalue=1, offvalue=0, command=opciones).pack()  # Crea y empaqueta un checkbutton con el texto "turismo", vinculado a la variable "turismo", con valor 1 al ser seleccionado y que llama a la función "opciones" cuando se selecciona.

textoFinal = Label(frame)  # Crea una etiqueta vacía en el marco.
textoFinal.pack()  # Empaqueta la etiqueta en el marco.

root.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
