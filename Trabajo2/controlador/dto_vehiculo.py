from dao.dao_vehiculo import VehiculoDAO
from models.vehiculo import Vehiculo
from database.db_connection import Connex
class VehiculoDTO:
    def __init__(self):
        self.dao = VehiculoDAO()
    
    #YA CAMBIO ACA
    def modificar(self, patente, marca, modelo, anio,precio,disponible):
        db = Connex()
        db.connect()
        vehiculo = Vehiculo(patente=patente,marca = marca,modelo = modelo,anio = anio, precio = precio,disponible = disponible)
        resultado = VehiculoDAO.modificar(db.connection, vehiculo)
        db.close()
        return resultado
    
    def eliminar(self, patente):
        db = Connex()
        db.connect()
        vehiculo = Vehiculo(patente=patente)
        resultado = VehiculoDAO.eliminar(db.connection, vehiculo)
        db.close()
        return resultado
    
    def listarDisponibilidad(self):
        db = Connex()
        db.connect()
        vehiculos = VehiculoDAO.listarDisponibilidad(db.connection)
        db.close()
        return vehiculos