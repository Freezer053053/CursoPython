from tkinter import *  # Importa todas las funciones y clases del módulo tkinter.
from tkinter import filedialog  # Importa el módulo filedialog de tkinter para mostrar cuadros de diálogo de archivos.

root = Tk()  # Crea la ventana principal de la aplicación.

def abreFichero():  # Define una función para abrir un archivo.
    fichero = filedialog.askopenfilename(
        title="Abrir",  # Establece el título del cuadro de diálogo.
        initialdir="C:/",  # Establece el directorio inicial donde se abrirá el cuadro de diálogo.
        filetypes=(  # Establece los tipos de archivos que se pueden abrir.
            ("Ficheros de excel", "*.xlsx"),
            ("Ficheros de texto", "*.txt"),
            ("Todos los ficheros", "*.*")
        )
    )
    print(fichero)  # Imprime en la consola la ruta del archivo seleccionado.

Button(root, text="Abrir fichero", command=abreFichero).pack()  # Crea y empaqueta un botón con el texto "Abrir fichero" que llama a la función abreFichero cuando se presiona.

root.mainloop()  # Inicia el bucle principal de la aplicación (hace que la ventana se mantenga abierta y reactiva).
