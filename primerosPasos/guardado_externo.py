import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print(f"Se ha creado una persona nueva con el nombre de {self.nombre}")

    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"
    
class listaPersonas:
    personas=[]

    def __init__(self):

        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print(f"Se cargaron {len(self.personas)} personas del fichero externo")

        except:
            print("El fichero está vacío")

        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonas(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def mostrarInfo(self):
        print("La información del fichero es: ")
        for p in self.personas:
            print(p)

miLista=listaPersonas()
p=Persona("Antonio", "Masculino", 32)
miLista.agregarPersonas(p)
miLista.mostrarInfo()


