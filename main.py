import tkinter as tk
import resolucion

class Aplicacion():
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry(resolucion.getResolucion())
        self.app.configure(bg = "red")
        self.app.title("RegiTravel")
        
        #Boton insertar
        self.insertarB = tk.Button(self.app, text="Insertar", command=quit, height = 5, width = 15, background="#8e99f3")
        self.insertarB["border"] = "0"
        self.insertarB.bind("<Enter>", lambda e:self.hover(e, self.insertarB))
        self.insertarB.bind("<Leave>", lambda e:self.unHover(e, self.insertarB))
        self.insertarB.grid(row=0, column=0, pady=10)

        #Boton eliminar
        self.eliminarB = tk.Button(self.app, text="Eliminar", command=quit, height = 5, width = 15, background="#8e99f3")
        self.eliminarB["border"] = "10"
        self.eliminarB.bind("<Enter>", lambda e:self.hover(e, self.eliminarB))
        self.eliminarB.bind("<Leave>", lambda e:self.unHover(e, self.eliminarB))
        self.eliminarB.grid(row=1, column=0, pady=10)

        #Boton consultar
        self.consultarB = tk.Button(self.app, text="Eliminar", command=quit, height = 5, width = 15, background="#8e99f3")
        self.consultarB["border"] = "3"
        self.consultarB.bind("<Enter>", lambda e:self.hover(e, self.consultarB))
        self.consultarB.bind("<Leave>", lambda e:self.unHover(e, self.consultarB))
        self.consultarB.grid(row=2, column=0,pady=10)

        #Boton guardar
        self.guardarB = tk.Button(self.app, text="Eliminar", command=quit, height = 5, width = 15, background="#8e99f3")
        self.guardarB["border"] = "3"
        self.guardarB.bind("<Enter>", lambda e:self.hover(e, self.guardarB))
        self.guardarB.bind("<Leave>", lambda e:self.unHover(e, self.guardarB))
        self.guardarB.grid(row=3, column=0,pady=10)

        #Boton cargar
        self.cargarB = tk.Button(self.app, text="Eliminar", command=quit,height = 5, width = 15, background="#8e99f3")
        self.cargarB["border"] = "3"
        self.cargarB.bind("<Enter>", lambda e:self.hover(e, self.cargarB))
        self.cargarB.bind("<Leave>", lambda e:self.unHover(e, self.cargarB))
        self.cargarB.grid(row=4, column=0, padx=10, pady=10)
        
        self.app.mainloop()

    def hover(self, e, boton):
        boton["background"] = "#26418f"
    
    def unHover(self, e, boton):
        boton["background"] = "#8e99f3"
 
    def insertar(self,e):
        self.insertarB["background"] = "green"
    
    def eliminar(self,e):
        self.insertarB["background"] = "orange"
    def consultar(self):
        pass
    def guardar(self):
        pass
    def cargar(self):
        pass
    

app = Aplicacion()