def funcion_decoradora(funcion_parametro):
    # Define una función interior que envuelve la función pasada como parámetro
    def funcion_interior():
        print("Vamos a realizar un cálculo:")  # Imprime un mensaje antes de ejecutar la función
        funcion_parametro()  # Llama a la función pasada como parámetro
        print("Cálculo realizado")  # Imprime un mensaje después de ejecutar la función
    return funcion_interior  # Retorna la función interior

# Aplica el decorador a la función 'suma'
@funcion_decoradora
def suma():
    print(3 + 5)  # Imprime el resultado de la suma

# Aplica el decorador a la función 'resta'
@funcion_decoradora
def resta():
    print(6 - 2)  # Imprime el resultado de la resta

# Llama a la función 'suma', que ahora está decorada
suma()

# Llama a la función 'resta', que ahora está decorada
resta()