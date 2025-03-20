def funcion_decoradora(funcion_parametro):
    # Define una función interior que envuelve la función pasada como parámetro
    def funcion_interior(*args):
        print("Vamos a realizar un cálculo:")  # Imprime un mensaje antes de ejecutar la función
        funcion_parametro(*args)  # Llama a la función pasada como parámetro con sus argumentos
        print("Cálculo realizado")  # Imprime un mensaje después de ejecutar la función
    return funcion_interior  # Retorna la función interior

# Aplica el decorador a la función 'suma'
@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)  # Imprime el resultado de la suma de tres números

# Aplica el decorador a la función 'resta'
@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)  # Imprime el resultado de la resta de dos números

# Llama a la función 'suma' con tres argumentos, que ahora está decorada
suma(2, 6, 8)

# Llama a la función 'resta' con dos argumentos, que ahora está decorada
resta(6, 3)