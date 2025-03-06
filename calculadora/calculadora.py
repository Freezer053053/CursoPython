from tkinter import *

root=Tk()
root.iconbitmap("calculadora/calc.ico")
root.title("Calculadora")
root.resizable(0,0)
root.config(bd="10")
root.config(relief="groove")


miFrame=Frame(root)
miFrame.pack()

operacion=""
resultado=0



#--------------------------------BotonPulsado----------------------

def botonPulsado(num):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        #operacion=""
    else: 
        numeroPantalla.set(numeroPantalla.get() + num)

#--------------------------------Función_suma----------------------

def suma(num):
    global operacion
    global resultado

    resultado+=int(num)

    operacion="suma"

    numeroPantalla.set(resultado)

#--------------------------------Función_resta----------------------

def resta(num):
    global operacion
    global resultado

    resultado+=int(num)

    operacion="resta"

    numeroPantalla.set(resultado)

#--------------------------------Función_mult----------------------

def mult(num):
    pass

#--------------------------------Función_resultadoFinal----------------------

def resultadoFinal():
    global resultado
    global operacion

    if operacion=="suma":
         resultado+=int(numeroPantalla.get())
    elif operacion=="resta":
        resultado-=int(numeroPantalla.get())

    numeroPantalla.set(resultado)
    resultado = 0
    operacion = ""

#--------------------------------Función_Reset----------------------

def reset():
    global resultado
    global operacion

    resultado=0
    operacion=""

    numeroPantalla.set("")


#----------------------Pantalla------------------------------------------------------#

numeroPantalla=StringVar()


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

botonMultiplicar=Button(miFrame, text="X", width=3, command=lambda:mult(numeroPantalla.get()))
botonMultiplicar.grid(row=2, column=4)
botonMultiplicar.config(bg="grey")

#----------------------Fila_2------------------------------------------------------#

boton4=Button(miFrame, text="4", width=3, command=lambda:botonPulsado("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=3, command=lambda:botonPulsado("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=3, command=lambda:botonPulsado("6"))
boton6.grid(row=3, column=3)

botonRestar=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRestar.grid(row=3, column=4)
botonRestar.config(bg="grey")

#----------------------Fila_3------------------------------------------------------#

boton1=Button(miFrame, text="1", width=3, command=lambda:botonPulsado("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=3, command=lambda:botonPulsado("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=3, command=lambda:botonPulsado("3"))
boton3.grid(row=4, column=3)

botonSumar=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSumar.grid(row=4, column=4)
botonSumar.config(bg="grey")

#----------------------Fila_4------------------------------------------------------#
botonComa=Button(miFrame, text=",", width=3)
botonComa.grid(row=5, column=1)

boton0=Button(miFrame, text="0", width=3, command=lambda:botonPulsado("0"))
boton0.grid(row=5, column=2)

botonIgual=Button(miFrame, text="=", width=3, command=lambda:resultadoFinal())
botonIgual.grid(row=5, column=3)
botonIgual.config(bg="green")

botonDividir=Button(miFrame, text="/", width=3)
botonDividir.grid(row=5, column=4)
botonDividir.config(bg="grey")

#----------------------Fila_5------------------------------------------------------#

botonBorrar=Button(miFrame, text="CE", width=3, command=lambda:reset())
botonBorrar.grid(row=6, column=1)
botonBorrar.config(bg="red")



root.mainloop()