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

    def toString(self):
        print("****************************")
        print("ID:", self.id,"Nombre de hotel: ",self.hotel,"Ciudad:",self.city,"Fecha:",self.date,"Nº habitaciones:",self.room)
        print("****************************")
    
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
