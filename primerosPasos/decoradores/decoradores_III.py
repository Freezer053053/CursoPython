def funcion_decoradora(funcion_parametro):
    # Define una función interior que envuelve la función pasada como parámetro
    def funcion_interior(*args, **kwargs):
        print("Vamos a realizar un cálculo:")  # Imprime un mensaje antes de ejecutar la función
        funcion_parametro(*args, **kwargs)  # Llama a la función pasada como parámetro con sus argumentos y argumentos clave
        print("Cálculo realizado")  # Imprime un mensaje después de ejecutar la función
    return funcion_interior  # Retorna la función interior

# Aplica el decorador a la función 'suma'
@funcion_decoradora
def suma(num1, num2, num3):
    """Suma dos números"""
    print(num1 + num2 + num3)  # Imprime el resultado de la suma de tres números

# Aplica el decorador a la función 'resta'
@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)  # Imprime el resultado de la resta de dos números

# Aplica el decorador a la función 'potencia'
@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))  # Imprime el resultado de elevar 'base' a la 'exponente'

# Llama a la función 'suma' con tres argumentos, que ahora está decorada
suma(2, 6, 8)

# Llama a la función 'resta' con dos argumentos, que ahora está decorada
resta(6, 3)

# Llama a la función 'potencia' con argumentos clave, que ahora está decorada
potencia(base=5, exponente=3)