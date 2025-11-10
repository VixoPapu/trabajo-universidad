from dao.dao_arriendo import ArriendoDAO
from database.db_connection import Connex
from models.arriendo import Arriendo
class ArriendoDTO:


    def IngresarArriendo(self, num_arriendo, fecha_inicio, fecha_entrega, costo_total, cliente, empleado, vehiculo):
        db = Connex()
        db.connect()
        arriendo = Arriendo(num_arriendo=num_arriendo, fecha_inicio=fecha_inicio, fecha_entrega=fecha_entrega, costo_total=costo_total, cliente=cliente, empleado=empleado, vehiculo=vehiculo)
        resultado = ArriendoDAO.insertar(db.connection, arriendo)
        db.close()
        return resultado
    
    
    def listarArriendo(self):
        db = Connex()
        db.connect()
        resultado = ArriendoDAO.listarArriendo(db.connection)
        db.close()
        return resultado