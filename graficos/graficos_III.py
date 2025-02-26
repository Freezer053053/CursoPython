from tkinter import *

root=Tk()

miFrame=Frame(root, width="500", height="400")
miFrame.pack()
#miFrame.pack(side=LEFT, anchor=N)

minombre=StringVar()

#---------------------------------------------------------#
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, pady=5, padx=10)
cuadroNombre.config(justify="center")

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e")
#---------------------------------------------------------#
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, pady=5, padx=10)
cuadroApellido.config(justify="center")

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e")
#---------------------------------------------------------#
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, pady=5, padx=10)
cuadroDireccion.config(justify="center")

direccionLabel=Label(miFrame, text="Direción de casa: ")
direccionLabel.grid(row=2, column=0, sticky="e")
#---------------------------------------------------------#
cuadroContraseña=Entry(miFrame)
cuadroContraseña.grid(row=3, column=1, pady=5, padx=10)
cuadroContraseña.config(justify="center", show="*")

contraseñaLabel=Label(miFrame, text="Contraseña: ")
contraseñaLabel.grid(row=3, column=0, sticky="e")
#---------------------------------------------------------#
textoComentarios=Text(miFrame, width=16, height=5)
textoComentarios.grid(row=4, column=1, pady=5, padx=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="e")

scrollVert=Scrollbar(miFrame, command=textoComentarios.yview)
scrollVert.grid(row=4, column=2, sticky=NSEW)               #Podemos escibirlo en mayusculas en vez de entre comillas

textoComentarios.config(yscrollcommand=scrollVert.set)      #para que el posicionador se localize en el area seleccionada
#---------------------------------------------------------#
 
def codigoBoton():
    minombre.set("Álex")

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()