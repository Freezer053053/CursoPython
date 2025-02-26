from tkinter import *

root=Tk()

miFrame=Frame(root, width="500", height="400")
miFrame.pack()

miImagen=PhotoImage(file="graficos/player.png")

#miLabel=Label(miFrame, text="Hola!", fg="red", font=("Comic Sans MS", 18))
#miLabel.place(x=250, y=250)

#Label(miFrame, text="Hola!").place(x=250, y=250)

miLabel=Label(miFrame, image=miImagen)
miLabel.place(x=250, y=250)


root.mainloop()