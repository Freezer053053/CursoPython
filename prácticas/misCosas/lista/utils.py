from tkinter import messagebox

def emergentes(error):
    match error:
        case "ya conectado":
            return messagebox.showerror("Error", "Actualmente ya estás conectado a la BBDD")
        case "conectar":
            return messagebox.showinfo("Conectar", "Conexión establecida con éxito")
        case "no_usuario":
            return messagebox.showerror("Error", "Seleccione un usuario")
        case "no se pudo conectar":
            return messagebox.showerror("Error", "Conexión fallida")
        case "tabla creada":
            return messagebox.showinfo("Info", "Tablas creadas correctamente")
        case "desconectar":
            return messagebox.showinfo("Desconectar", "Desconectado de la BBDD con éxito")
        case "no_conectado":
            return messagebox.showinfo("Info", "Aún no estas conectado a la BBDD")
        case "conectado":
            return messagebox.showinfo("Info", "Conectado a tablas existentes: Capacitores, Diodos, Resistencias, Chips y Transistores")
        
