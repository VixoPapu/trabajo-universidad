from dao.dao_arriendo import ArriendoDAO
from database.db_connection import Connex
from models.arriendo import Arriendo
from models.conversion import Conversion
from models.cliente import Cliente
from models.empleado import Empleado
from models.vehiculo import Vehiculo

class ArriendoDTO:

    def ingresarArriendo(self, num_arriendo: int, fecha_inicio, fecha_entrega, costo_total: Conversion,
                         cliente: Cliente, empleado: Empleado, vehiculo: Vehiculo):
        db = Connex()
        db.connect()
        try:
            arriendo = Arriendo(num_arriendo, fecha_inicio, fecha_entrega, costo_total, cliente, empleado, vehiculo)
            resultado = ArriendoDAO.insertarArriendo(db.connection, arriendo)
        finally:
            db.close()
        return resultado

    def listarArriendo(self):
        db = Connex()
        db.connect()
        resultado = ArriendoDAO.listarArriendos(db.connection) 
        db.close()
        return resultado
