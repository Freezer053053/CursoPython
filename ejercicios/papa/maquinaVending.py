def calcular_cambio(costo, dinero):
    monedas_y_billetes=[1000, 500, 200, 100, 50, 20]
    cambio=[]
    diferencia = dinero - costo
    
    if diferencia<0:
        return "No hay suficiente dinero"
    
    diferencia=int(diferencia * 100)