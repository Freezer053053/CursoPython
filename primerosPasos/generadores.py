def generaPares(limite):
    num=1

    while num<limite:
        yield num*2
        num+=1

devuevePares=generaPares(10)

print(next(devuevePares))

print("Aquí iría más código...")

print(next(devuevePares))

print("Aquí iría más código...")

print(next(devuevePares))