from models.arriendo import Arriendo
class ArriendoDAO:

    def IngresarArriendo(conn, arriendo):
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO Arriendos (num_arriendo, fecha_inicio, fecha_entrega, costo_total, run_cliente, codigo_empleado, patente_vehiculo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                arriendo.getNumArriendo(),
                arriendo.getFechaInicio(),
                arriendo.getFechaEntrega(),
                arriendo.getCostoTotal(),
                arriendo.getCliente(),
                arriendo.getEmpleado(),
                arriendo.getVehiculo()
            ))
            conn.commit()
            cursor.close()
            return "Arriendo creado correctamente"
        except Exception as e:
            return f"Error al insertar Arriendo: {str(e)}"



    def listarArriendo(conn):
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM Arriendos"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            
            Arriendo = []
            for resultado in resultados:
                arriendo = Arriendo(
                    num_arriendo=resultado[0],
                    fecha_inicio=resultado[1],
                    fecha_entrega=resultado[2],
                    costo_total=resultado[3],
                    run_cliente=resultado[4],
                    codigo_empleado=resultado[5],
                    patente_vehiculo=resultado[6]

                )
                arriendo.append(arriendo)
            return arriendo
        except Exception as e:
            print(f"Error al listar arriendos: {str(e)}")
            return []
