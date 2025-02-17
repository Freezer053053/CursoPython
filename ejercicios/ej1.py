def DevuelveMax(a, b):
    if a<b:
        return b
    else:
        return a

num1=int(input("introduce un número: "))
num2=int(input("introduce otro número: "))

print("El número mas alto es: ", DevuelveMax(num1, num2))