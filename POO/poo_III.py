class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculos(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camion()

desplazamientoVehiculos(miVehiculo)