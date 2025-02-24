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

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class Moto(Vehiculos):

    do_wheelie=""
    def wheelie(self):
        self.do_wheelie="Haciendo wheelie"
    
    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\n{self.do_wheelie}")

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

miMoto=Moto("Honda", "CBR")

miMoto.wheelie()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class bicicletaElectrica(VElectricos, Vehiculos):
    pass

miBici=bicicletaElectrica("Orbea", "XB1200")




