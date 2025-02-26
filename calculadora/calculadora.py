from tkinter import *

root=Tk()
root.iconbitmap("calculadora/calc.ico")
root.title("Calculadora")
root.resizable(0,0)

miFrame=Frame(root)
miFrame.pack()

operacion=""

accion=""

nums=[]

numeroPantalla=StringVar()

#--------------------------------BotonPulsado----------------------

def botonPulsado(num):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else: 
        numeroPantalla.set(numeroPantalla.get() + num)
        
    


#--------------------------------Función_suma----------------------

def suma():
    global operacion
    operacion="suma"


#----------------------Pantalla------------------------------------------------------#

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="green", justify=RIGHT)

#----------------------Fila_1------------------------------------------------------#

boton7=Button(miFrame, text="7", width=3, command=lambda:botonPulsado("7"))
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width=3, command=lambda:botonPulsado("8"))
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width=3, command=lambda:botonPulsado("9"))
boton9.grid(row=2, column=3)

botonMultiplicar=Button(miFrame, text="X", width=3)
botonMultiplicar.grid(row=2, column=4)

#----------------------Fila_2------------------------------------------------------#

boton4=Button(miFrame, text="4", width=3, command=lambda:botonPulsado("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=3, command=lambda:botonPulsado("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=3, command=lambda:botonPulsado("6"))
boton6.grid(row=3, column=3)

botonRestar=Button(miFrame, text="-", width=3)
botonRestar.grid(row=3, column=4)

#----------------------Fila_3------------------------------------------------------#

boton1=Button(miFrame, text="1", width=3, command=lambda:botonPulsado("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=3, command=lambda:botonPulsado("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=3, command=lambda:botonPulsado("3"))
boton3.grid(row=4, column=3)

botonSumar=Button(miFrame, text="+", width=3, command=lambda:suma)
botonSumar.grid(row=4, column=4)

#----------------------Fila_4------------------------------------------------------#

botonDividir=Button(miFrame, text="/", width=3)
botonDividir.grid(row=5, column=1)

boton0=Button(miFrame, text="0", width=3)
boton0.grid(row=5, column=2)

botonComa=Button(miFrame, text=",", width=3)
botonComa.grid(row=5, column=3)

botonIgual=Button(miFrame, text="=", width=3)
botonIgual.grid(row=5, column=4)





root.mainloop()