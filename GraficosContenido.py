import tkinter as tk
import time


class Insertar:
    def __init__(self, padre):
        # self.contenedorEliminar = tk.Frame(padre)
        # self.contenedorEliminar.place(relwidth=1, relheight=1, relx=0,rely=0)
        contenedor = tk.Frame(padre, relief="groove", borderwidth=2)
        contenedor.place(relwidth=1, relheight=0.8, relx=0,rely=0)

        self.idL = tk.Label(contenedor, text="Id de Reserva:", font = "Verdana 25 bold italic", relief="groove")
        self.idL.place(relwidth=0.5, relheight=0.2, relx=0,rely=0)
        self.idE = tk.Entry(contenedor, font = "Verdana 25")
        self.idE.place(relwidth=0.5, relheight=0.2, relx=0.5,rely=0)

        self.HotelL = tk.Label(contenedor, text="Nombre de Hotel", font = "Verdana 25 bold italic", relief="groove")
        self.HotelL.place(relwidth=0.5, relheight=0.2, relx=0,rely=0.2)
        self.HotelE = tk.Entry(contenedor, font = "Verdana 25")
        self.HotelE.place(relwidth=0.5, relheight=0.2, relx=0.5,rely=0.2)

        self.CiudadL = tk.Label(contenedor, text="Ciudad", font = "Verdana 25 bold italic", relief="groove")
        self.CiudadL.place(relwidth=0.5, relheight=0.2, relx=0,rely=0.4)
        self.CiudadE = tk.Entry(contenedor, font = "Verdana 25")
        self.CiudadE.place(relwidth=0.5, relheight=0.2, relx=0.5,rely=0.4)
        
        self.FechaL = tk.Label(contenedor, text="Fecha", font = "Verdana 25 bold italic", relief="groove")
        self.FechaL.place(relwidth=0.5, relheight=0.2, relx=0,rely=0.6)
        self.FechaE = tk.Entry(contenedor, font = "Verdana 25")
        self.FechaE.place(relwidth=0.5, relheight=0.2, relx=0.5,rely=0.6)
        self.getFecha()

        self.HabitacionesL = tk.Label(contenedor, text="Número de Habitaciones", font = "Verdana 25 bold italic", relief="groove")
        self.HabitacionesL.place(relwidth=0.5, relheight=0.2, relx=0,rely=0.8)
        self.HabitacionesE = tk.Entry(contenedor, font = "Verdana 25")
        self.HabitacionesE.place(relwidth=0.5, relheight=0.2, relx=0.5,rely=0.8)

        #Botones de aceptar
        self.insertarB = tk.Button(padre, text="Aceptar", bg="#2cb978", command=self.getFecha)
        self.insertarB.place(relwidth=0.20, relheight=0.10, relx=0.3,rely=0.85)

        self.cancelarB = tk.Button(padre, text="Cancelar", bg="#f85959", command=quit)
        self.cancelarB.place(relwidth=0.20, relheight=0.10, relx=0.5,rely=0.85)

    def getFecha(self):
        self.FechaE.config(state=tk.NORMAL)
        self.FechaE.delete(0,tk.END)
        now = time.strftime("%m/%d/%Y, %H:%M:%S")
        print(type(now))
        self.FechaE.insert(0,now)
        self.FechaE.config(state="readonly")
#IdReserva, Hotel, Ciudad, Fecha, Habitacciones

class Mostrar:
    def __init__(self, padre):
        self.lFrame = tk.LabelFrame(padre, text="This is a LabelFrame")
        self.lFrame.pack(fill="both", expand="yes")
