import tkinter as tk
import GraficosContenido as ventanas
import time

class Aplicacion():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        
        self.cabecera = Cabecera(self.root)
        self.general = Cuerpo(self.root)
        
        self.root.title("RegiTravel")
        self.root.mainloop()


class Cabecera():
    def __init__(self, padre):
        self.frame = tk.Frame(padre)
        self.frame.place(relwidth=1, relheight=0.15, relx=0,rely=0)
        self.titulo = tk.Label(self.frame, text="RegiTravel",bg="#3b83bd",font = "Verdana 50 bold italic")
        self.titulo.place(relwidth=1, relheight=1, relx=0,rely=0)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%m/%d/%Y, %H:%M:%S")
        self.titulo.configure(text=now)
        self.frame.after(1000, self.update_clock)

class Cuerpo():
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg="#FFFFFF")
        self.frame.place(relwidth=1, relheight=0.85,relx=0,rely=0.15)
        self.menu = tk.Frame(self.frame,bg="#D0D3D4")
        self.menu.place(relwidth=0.16, relheight=1,relx=0,rely=0)
        self.contenido = tk.Frame(self.frame, bg="#FFFFFF")
        self.contenido.place(relwidth=0.68, relheight=1,relx=0.16,rely=0)
        self.lateralIzq = tk.Frame(self.frame, bg="#FFFFFF", relief="groove", borderwidth=2)
        self.lateralIzq.place(relwidth=0.16, relheight=1,relx=0.84,rely=0)
        menu = Menu(self.menu, self.contenido)

class Menu():
    def __init__(self, padre, contenido):
        #Boton insertar
        self.insertarB = tk.Button(padre, text="Insertar", command=lambda:self.insertarV(contenido), height = 5, width = 15, background="#8e99f3")
        self.insertarB["border"] = "2"
        self.insertarB.bind("<Enter>", lambda e:self.hover(self.insertarB))
        self.insertarB.bind("<Leave>", lambda e:self.unHover(self.insertarB))
        self.insertarB.place(relwidth=0.8, relheight=0.13,relx=0.1,rely=0.04)

        #Boton eliminar
        self.eliminarB = tk.Button(padre, text="Mostrar", command=lambda:self.mostrarV(contenido), height = 5, width = 15, background="#8e99f3")
        self.eliminarB["border"] = "2"
        self.eliminarB.bind("<Enter>", lambda e:self.hover(self.eliminarB))
        self.eliminarB.bind("<Leave>", lambda e:self.unHover(self.eliminarB))
        self.eliminarB.place(relwidth=0.8, relheight=0.13,relx=0.1,rely=0.20)

        #Boton consultar
        self.consultarB = tk.Button(padre, text="Eliminar", command=quit, height = 5, width = 15, background="#8e99f3")
        self.consultarB["border"] = "2"
        self.consultarB.bind("<Enter>", lambda e:self.hover(self.consultarB))
        self.consultarB.bind("<Leave>", lambda e:self.unHover(self.consultarB))
        self.consultarB.place(relwidth=0.8, relheight=0.13,relx=0.1,rely=0.36)

        #Boton guardar
        self.guardarB = tk.Button(padre, text="Importar", command=quit, height = 5, width = 15, background="#8e99f3")
        self.guardarB["border"] = "2"
        self.guardarB.bind("<Enter>", lambda e:self.hover(self.guardarB))
        self.guardarB.bind("<Leave>", lambda e:self.unHover(self.guardarB))
        self.guardarB.place(relwidth=0.8, relheight=0.13,relx=0.1,rely=0.52)

        #Boton cargar
        self.cargarB = tk.Button(padre, text="Cargar", command=quit,height = 5, width = 15, background="#8e99f3")
        self.cargarB["border"] = "2"
        self.cargarB.bind("<Enter>", lambda e:self.hover(self.cargarB))
        self.cargarB.bind("<Leave>", lambda e:self.unHover(self.cargarB))
        self.cargarB.place(relwidth=0.8, relheight=0.13,relx=0.1,rely=0.68)

        #Boton salir
        self.salirB = tk.Button(padre, text="salir", command= lambda:self.salirAplicacion(padre), bg="#CD5C5C", height = 5, width = 15)
        self.salirB["border"] = "2"
        self.salirB.place(relwidth=0.8, relheight=0.13,relx=0.1,rely=0.84)

    def hover(self, boton):
        boton["background"] = "#26418f"
    
    def unHover(self, boton):
        boton["background"] = "#8e99f3"
    def salirAplicacion(self, principal):
        #Sacar las cordenadas para establecer esta ventana en el centro
        confirmar = tk.Toplevel(principal)
        confirmar.grab_set()
        confirmar.geometry("300x300")
        confirmar.title("Confirmar")
        pregunta = tk.Label(confirmar,text="¿Quieres salir de la aplicación?")
        pregunta.place(relwidth=1, relheight=0.5, relx=0,rely=0)
        #Botones
        aceptar = tk.Button(confirmar,text="Salir",command=quit,bg="orange")
        aceptar.place(relwidth=0.5, relheight=0.5, relx=0,rely=0.5)

        cancelar = tk.Button(confirmar, text="Cancelar", command = lambda:confirmar.destroy(),bg="green")

        cancelar.place(relwidth=0.5, relheight=0.5, relx=0.5,rely=0.5)
    def insertarV(self,padre):
        padre.place_forget()
        padre.place(relwidth=0.68, relheight=1,relx=0.16,rely=0)
        frameDesechable = tk.Frame(padre)
        frameDesechable.place(relwidth=1, relheight=1, relx=0,rely=0)
        insercion = ventanas.Insertar(padre)

    def mostrarV(self, padre):
        print("mostrarV")
        padre.place_forget()
        padre.place(relwidth=0.68, relheight=1,relx=0.16,rely=0)
        frameDesechable = tk.Frame(padre)
        frameDesechable.place(relwidth=1, relheight=1,relx=0,rely=0)
        mostrar = ventanas.Mostrar(frameDesechable)

app = Aplicacion()
