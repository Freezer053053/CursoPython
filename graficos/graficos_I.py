from tkinter import *

raiz=Tk()

raiz.title("Ventana")

raiz.resizable(1,1)

raiz.iconbitmap("graficos/icono.ico")

#raiz.geometry("800x600")

raiz.config(bg="blue")
raiz.config(bd="35")
raiz.config(relief="groove")

miFrame=Frame()

#miFrame.pack(side="right", anchor="n")
#miFrame.pack(fill="x")
#miFrame.pack(fill="y", expand="True")
#miFrame.pack(fill="both", expand="True")
miFrame.pack()

miFrame.config(bg="blue")

miFrame.config(width="650", height="350")

miFrame.config(bd="35")
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")

raiz.mainloop()