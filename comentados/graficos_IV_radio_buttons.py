from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.

root = Tk()  # Crea la ventana principal de la aplicación.

varOpcion = IntVar()  # Declara una variable de tipo IntVar para almacenar enteros, utilizada para los radiobuttons.

def imprimir():  # Define una función que se ejecuta cuando se selecciona un radiobutton.
    # print(varOpcion.get())  # Imprime en la consola el valor actual de varOpcion (comentado).

    if varOpcion.get() == 1:  # Si el valor de varOpcion es 1...
        etiqueta.config(text="Has elegido masculino")  # ...cambia el texto de la etiqueta a "Has elegido masculino".
    elif varOpcion.get() == 2:  # Si el valor de varOpcion es 2...
        etiqueta.config(text="Has elegido femenino")  # ...cambia el texto de la etiqueta a "Has elegido femenino".

Label(root, text="Género:").pack()  # Crea y empaqueta una etiqueta con el texto "Género:" en la ventana principal.

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=lambda: imprimir()).pack()  # Crea y empaqueta un radiobutton con el texto "Masculino", vinculado a varOpcion, con valor 1 y que llama a imprimir() cuando se selecciona.
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=lambda: imprimir()).pack()  # Crea y empaqueta un radiobutton con el texto "Femenino", vinculado a varOpcion, con valor 2 y que llama a imprimir() cuando se selecciona.

etiqueta = Label(root)  # Crea una etiqueta vacía en la ventana principal.
etiqueta.pack()  # Empaqueta la etiqueta en la ventana principal.

root.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
