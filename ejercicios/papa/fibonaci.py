def fibonacci(n):
    sequencia=[]
    a, b = 0, 1
    for i in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

def operacionPrincipal():
    try:
        num=int(input("Cuántos números de fibonacci quieres? "))
        if num<=0:
            print("Introduce un número válido")
        else:
            sequencia_fib=fibonacci(num)
            print("Secuencia de fibonacci:")
            for numero in sequencia_fib:
                print(numero)
    except ValueError:
        print("Introduce un número válido")

operacionPrincipal()