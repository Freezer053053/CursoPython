def calcular_cambio(costo, dinero_proporcionado):
    billetes_monedas = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    cambio = []
    diferencia = dinero_proporcionado - costo

    if diferencia < 0:
        return []

    diferencia = int(diferencia * 100)

    for valor in billetes_monedas:
        while diferencia >= valor:
            cambio.append(valor / 100)
            diferencia -= valor

    return cambio

costo = float(input("Introduce el costo del producto: "))
dinero_proporcionado = float(input("Introduce el dinero a meter: "))
cambio = calcular_cambio(costo, dinero_proporcionado)

if len(cambio) < 0:
    print("No hay suficiente dinero")
else:
    print("Tu cambio es:", cambio)