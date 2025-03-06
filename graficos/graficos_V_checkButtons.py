from tkinter import *


root=Tk()
root.title("CheckButtons")

playa=IntVar()
montagna=IntVar()
turismo=IntVar()

def opciones():
    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" playa"

    if(montagna.get()==1):
        opcionEscogida+=" montaña"

    if(turismo.get()==1):
        opcionEscogida+=" turismo"

    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="graficos/avion.png")
Label(root, image=foto).pack()
frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame, text="montaña", variable=montagna, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame, text="turismo", variable=turismo, onvalue=1, offvalue=0, command=opciones).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()