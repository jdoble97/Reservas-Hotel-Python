import json
import os.path as path

class Reserva:
    """
    Se ha definido una clase Reserva para simplificar la forma de añadir reservas
    """
    def __init__(self,idReserva, hotel, ciudad, fecha,habitaciones):
        self.id = idReserva
        self.hotel = hotel
        self.city = ciudad
        self.date = fecha
        self.room = habitaciones
    
    def datosReserva(self):
        datoReserva = "ID: "+self.id+" -> Hotel: "+self.hotel
        return datoReserva
    
    def getInformacionDetallada(self):
        detalles = []
        detalles.append("ID: "+self.id)
        detalles.append("Hotel: "+self.hotel)
        detalles.append("Ciudad: "+self.city)
        detalles.append("Fecha: "+self.date)
        detalles.append("Habitaciones: "+self.room)
        return detalles
    
    @staticmethod
    def getReservaDeseada(idReserva, listaReservas=[]):
        for x in listaReservas:
            if idReserva==x.id:
                return x
    
    @staticmethod
    def eliminarReservaDeseada(reservaEliminar, listaReservas=[]):
        if reservaEliminar in listaReservas:
            listaReservas.remove(reservaEliminar)

class Fichero:
    def __init__(self):
        pass

    @staticmethod
    def exportar(listaReserva=[]):
    
        listaJson = []
        for elemento in listaReserva:
            listaJson.append({
                "id" : elemento.id,
                "hotel" : elemento.hotel,
                "city" : elemento.city,
                "date" : elemento.date,
                "room" : elemento.room})
        with open('data.json', 'w') as file:
            json.dump(listaJson, file, indent=4)
    
    @staticmethod
    def cargar(listaReservas):
        if path.exists("data.json"):
            listaReservas.clear()
            with open('data.json') as json_file:
                data = json.load(json_file)
                for x in data:
                    atributos = []
                    for k in x:
                        atributos.append(x[k])
                    listaReservas.append(Reserva(atributos[0],atributos[1],atributos[2],atributos[3],atributos[4]))
