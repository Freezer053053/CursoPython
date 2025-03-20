capacitor = Tk()
    capacitor.title("Capacitores")
    capacitor.geometry('224x100')
    frameCap = Frame(capacitor)
    frameCap.pack()

    tipo = ttk.Combobox(frameCap,
                      state = "readonly",
                      values = ["Electrolítico","Electrolítico SMD", "Cerámico", "Cerámico SMD", "Film", "Mica", "Variable"]
                      )
    tipo.grid(row = 0, column = 0, pady = 10)

    polarizado = ttk.Combobox(frameCap,
                      state = "readonly",
                      values = ["Si", "No"]
                      )
    polarizado.grid(row = 1, column = 0, pady = 10)