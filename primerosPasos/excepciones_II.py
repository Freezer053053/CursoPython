def divide():

    try:
        op1=float(input("Introduce el primer número: "))
        op2=float(input("Introduce el segundo número: "))

        print("La división es: " + str(op1/op2))
    
    except ValueError:
        print("El valor introducido es erróneo")
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    finally:    # Se ejecuta el codigo siempre
        print("Cálculo finalizado")

divide()
