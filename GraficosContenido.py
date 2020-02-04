import tkinter as tk
from tkinter import messagebox
import time
from Reserva import Reserva
import uuid
from informacion import info


class Insertar:
    def __init__(self, padre, reservasGlobales):
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
        self.insertarB = tk.Button(padre, text="Aceptar", bg="#2cb978", command=lambda:self.insertarReservaFormulario(reservasGlobales))
        self.insertarB.place(relwidth=0.20, relheight=0.10, relx=0.3,rely=0.85)

        self.cancelarB = tk.Button(padre, text="Cancelar", bg="#f85959", command=quit)
        self.cancelarB.place(relwidth=0.20, relheight=0.10, relx=0.5,rely=0.85)

    def getFecha(self):
        idForm = str(uuid.uuid1().int)[:20]
        self.idE.delete(0,tk.END)
        self.idE.insert(0,idForm)
        self.FechaE.config(state=tk.NORMAL)
        self.FechaE.delete(0,tk.END)
        now = time.strftime("%m/%d/%Y, %H:%M:%S")
        self.FechaE.insert(0,now)
        self.FechaE.config(state="readonly")
    
    def insertarReservaFormulario(self, listadeReservas=[]):
        
        
        datosComprobar = [self.HotelE.get(),self.CiudadE.get(),self.HabitacionesE.get()]
        if not datosComprobar[0] or not datosComprobar[1] or not datosComprobar[2]:
            print("Esta vacio")
            messagebox.showwarning(message="Debes rellenar todos los campos",title="Aviso")
        else:
            self.getFecha()
            resFormObj = Reserva(self.idE.get(),self.HotelE.get(),self.CiudadE.get(),self.FechaE.get(),
            self.HabitacionesE.get())
            listadeReservas.append(resFormObj)
            self.limpiarFormulario()
            messagebox.showinfo(message="Has rellenado correctamente el formulario",title="Correcto")


    
    def limpiarFormulario(self):
        self.HotelE.delete(0,tk.END)
        self.CiudadE.delete(0,tk.END)
        self.HabitacionesE.delete(0,tk.END)
        self.getFecha()

        
#IdReserva, Hotel, Ciudad, Fecha, Habitacciones

class Mostrar:
    def __init__(self, padre, reservasGlobales):
        self.frameReservas = tk.Frame(padre, bg="red")
        self.frameReservas.place(relwidth=0.30, relheight=1, relx=0,rely=0)
        self.listaReservas = tk.Listbox(self.frameReservas, bg="white")
        self.listaReservas.place(relwidth=1, relheight=0.75, relx=0,rely=0)
        self.listarReservasF(reservasGlobales)
        self.listaReservas.select_set(0)
        
        #Botones
        self.mostrarReserva = tk.Button(self.frameReservas, text="Mostrar", command=lambda:self.mostrarCaracteristicasReserva(reservasGlobales))
        self.mostrarReserva.place(relwidth=0.4, relheight=0.1, relx=0.3,rely=0.8)

        #Labels para la informacion
        self.idL = tk.Label(padre, text="ID", font = "Verdana 25 bold italic", relief="groove")
        self.idL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0)
        self.HotelL = tk.Label(padre, text="Nombre de Hotel", font = "Verdana 25 bold italic", relief="groove")
        self.HotelL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.2)
        self.CiudadL = tk.Label(padre, text="Ciudad", font = "Verdana 25 bold italic", relief="groove")
        self.CiudadL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.4)
        self.FechaL = tk.Label(padre, text="Fecha", font = "Verdana 25 bold italic", relief="groove")
        self.FechaL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.6)
        self.HabitacionesL = tk.Label(padre, text="Número de Habitaciones", font = "Verdana 25 bold italic", relief="groove")
        self.HabitacionesL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.8)

        

    def listarReservasF(self, reservasMostrar=[]):
        resumenReserva = []
        for res in reservasMostrar:
            resumenReserva.append(res.datosReserva())

        self.listaReservas.insert(0,*resumenReserva)
    def mostrarCaracteristicasReserva(self, reservasGlobales):
        prueba = self.listaReservas.selection_get()
        idSeleccionado = prueba.split(" ")[1]
        print("Esto es: "+idSeleccionado)
        reservaSeleccionada = Reserva.getReservaDeseada(idSeleccionado, reservasGlobales)
        detallesReserva = reservaSeleccionada.getInformacionDetallada()
        self.idL["text"]= detallesReserva[0]
        self.HotelL["text"] = detallesReserva[1]
        self.CiudadL["text"] = detallesReserva[2]
        self.FechaL["text"] = detallesReserva[3]
        self.HabitacionesL["text"] = detallesReserva[4]

        print(prueba)

class Eliminar: 
    def __init__(self, padre, reservasGlobales):
        self.reservaQueEliminamos = None
        self.frameReservas = tk.Frame(padre, bg="red")
        self.frameReservas.place(relwidth=0.30, relheight=1, relx=0,rely=0)
        self.listaReservas = tk.Listbox(self.frameReservas, bg="white")
        self.listaReservas.place(relwidth=1, relheight=0.75, relx=0,rely=0)
        self.listarReservas(reservasGlobales)
        self.listaReservas.select_set(0)
        
        #Botones
        self.mostrarReserva = tk.Button(self.frameReservas, text="Mostrar", command=lambda:self.mostrarCaracteristicasReserva(reservasGlobales))
        self.mostrarReserva.place(relwidth=0.4, relheight=0.1, relx=0.1,rely=0.8)
        self.eliminarReserva = tk.Button(self.frameReservas, text="Eliminar", command=lambda:self.aceptarEliminar(reservasGlobales), state=tk.DISABLED)
        self.eliminarReserva.place(relwidth=0.4, relheight=0.1, relx=0.5,rely=0.8)
        

        #Labels para la informacion
        self.idL = tk.Label(padre, text="ID" ,font = "Verdana 25 bold italic", relief="groove")
        self.idL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0)
        self.HotelL = tk.Label(padre, text="Nombre de Hotel", font = "Verdana 25 bold italic", relief="groove")
        self.HotelL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.2)
        self.CiudadL = tk.Label(padre, text="Ciudad", font = "Verdana 25 bold italic", relief="groove")
        self.CiudadL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.4)
        self.FechaL = tk.Label(padre, text="Fecha", font = "Verdana 25 bold italic", relief="groove")
        self.FechaL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.6)
        self.HabitacionesL = tk.Label(padre, text="Número de Habitaciones", font = "Verdana 25 bold italic", relief="groove")
        self.HabitacionesL.place(relwidth=0.7, relheight=0.2, relx=0.3,rely=0.8)
        self.comprobarReservasTam(reservasGlobales)

    def listarReservas(self, reservasMostrar=[]):
        self.listaReservas.delete(0,tk.END)
        resumenReserva = []
        for res in reservasMostrar:
            resumenReserva.append(res.datosReserva())

        self.listaReservas.insert(0,*resumenReserva)
    
    def aceptarEliminar(self, reservasGlobal=[]):
        if len(reservasGlobal)==0:
            self.eliminarReserva["state"] = tk.DISABLED
            self.mostrarReserva["state"] = tk.DISABLED
        else:
            print("aceptarEliminar funcion")
            respuesta = messagebox.askyesno(message="¿Estás seguro de querer eliminar esta reserva?", title="Seguro de eliminar")
        # print(messagebox.askokcancel(message="¿Desea continuar?", title="Título"))
        # print(messagebox.askretrycancel(message="¿Desea reintentar?", title="Título"))
            if respuesta:
                Reserva.eliminarReservaDeseada(self.reservaQueEliminamos, reservasGlobal)
            self.listarReservas(reservasGlobal)
            self.comprobarReservasTam(reservasGlobal)
    
    def mostrarCaracteristicasReserva(self, reservasGlobales):
        self.eliminarReserva["state"] = tk.ACTIVE
        prueba = self.listaReservas.selection_get()
        idSeleccionado = prueba.split(" ")[1]
        print("Esto es: "+idSeleccionado)
        reservaSeleccionada = Reserva.getReservaDeseada(idSeleccionado, reservasGlobales)
        detallesReserva = reservaSeleccionada.getInformacionDetallada()
        self.idL["text"]= detallesReserva[0]
        self.HotelL["text"] = detallesReserva[1]
        self.CiudadL["text"] = detallesReserva[2]
        self.FechaL["text"] = detallesReserva[3]
        self.HabitacionesL["text"] = detallesReserva[4]
        self.reservaQueEliminamos = reservaSeleccionada
        print(prueba)

    def comprobarReservasTam(self, reservasGlobales):
        if len(reservasGlobales)==0:
            self.eliminarReserva["state"] = tk.DISABLED
            self.mostrarReserva["state"] = tk.DISABLED
        else:
            self.listaReservas.select_set(0)
            self.eliminarReserva["state"] = tk.DISABLED
        
        self.idL["text"]= "ID"
        self.HotelL["text"] = "Nombre de Hotel"
        self.CiudadL["text"] = "Ciudad"
        self.FechaL["text"] = "Fecha"
        self.HabitacionesL["text"] = "Numero de habitaciones"


class Informacion:
    def __init__(self, padre):
        self.listaReservas = tk.Listbox(padre, bg="white", font = "Verdana 11 bold italic")
        self.listaReservas.place(relwidth=1, relheight=1, relx=0,rely=0)
        self.listaReservas.insert(0,*info)
        self.horaL = tk.Label(padre,bg="green", font = "Verdana 11 bold italic")
        self.horaL.place(relwidth=1, relheight=0.2, relx=0,rely=0.8)
        self.update_clock(padre)
    
    def update_clock(self, padre):
        now = time.strftime("%m/%d/%Y, %H:%M:%S")
        self.horaL.configure(text=now)
        padre.after(1000, lambda:self.update_clock(padre))
