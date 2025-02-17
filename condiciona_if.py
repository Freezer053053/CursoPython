print("Programa evaluacion de notas")

nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
    valoracion="aprovado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno))) #Transformamos el str a int