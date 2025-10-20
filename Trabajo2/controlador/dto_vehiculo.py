from dao.dao_vehiculo import VehiculoDAO
from database.db_connection import Connex
class VehiculoDTO:
    def __init__(self):
        self.dao = VehiculoDAO()
    
    def modificar(self, vehiculo):
        db = Connex()
        db.connect()
        resultado = VehiculoDAO.modificar(db.connection, vehiculo)
        db.close()
        return resultado
    
    def eliminar(self, patente):
        db = Connex()
        db.connect()
        resultado = VehiculoDAO.eliminar(db.connection, patente)
        db.close()
        return resultado
    
    def listarDisponibilidad(self):
        db = Connex()
        db.connect()
        vehiculos = VehiculoDAO.listarDisponibilidad(db.connection)
        db.close()
        return vehiculos