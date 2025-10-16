from models.arriendo import Arriendo

class ArriendoDb:
    def insertar(conn, arriendo:Arriendo):
        sql = """
        INSERT INTO arriendos (num_arriendo, fecha_inicio, fecha_entrega, costo_total, run_cliente, codigo_empleado, patente_vehiculo)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
