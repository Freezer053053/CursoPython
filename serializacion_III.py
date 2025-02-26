import pickle

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}")

coche1=Vehiculos("Opel", "Astra")
coche2=Vehiculos("Seat", "Ibiza")
coche3=Vehiculos("Renault", "Leon")

coches=[coche1, coche2, coche3]

fichero=open("coches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

fichero_apertura=open("coches", "rb")

misCoches=pickle.load(fichero_apertura)

fichero_apertura.close()

for i in misCoches:
    print(i.estado())