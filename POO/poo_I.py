class Coche():

    def __init__(self): #Constructor
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #Encapsulada
        self.__enmarcha=False

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        
        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche está arrancado"
        elif (self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche no está arrancado"

    
    def estado(self):
        print("El coche tiene ", self.__ruedas, ", un ancho de ", self.__anchoChasis, " y una largo de ", self.__largoChasis)
    
    def __chequeo_interno(self):
        print("Relizando chequeo")

        self.gas="ok"
        self.oil="ok"
        self.doors="closed"

        if (self.gas=="ok" and self.oil=="ok" and self.doors=="closed"):
            return True
        else:
            return False

miCoche=Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("---------------Segundo-Objeto---------------")

miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()