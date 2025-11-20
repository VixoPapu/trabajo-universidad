from models.arriendo import Arriendo
from models.conversion import Conversion
from models.cliente import Cliente
from models.empleado import Empleado
from models.vehiculo import Vehiculo

class ArriendoDAO:

    @staticmethod
    def insertarArriendo(conn, arriendo: Arriendo):
        try:
            cursor = conn.cursor()
            sql = """
            INSERT INTO arriendos
            (num_arriendo, fecha_inicio, fecha_entrega, costo_total_uf, run_cliente, codigo_empleado, patente_vehiculo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                arriendo.getNumArriendo(),
                arriendo.getFechaInicio(),
                arriendo.getFechaEntrega(),
                arriendo.getCostoTotal().getCosto(),  # usar el valor de Conversion
                arriendo.getCliente().getRun(),       # solo el RUN del cliente
                arriendo.getEmpleado().getCodigo(),   # solo el código del empleado
                arriendo.getVehiculo().getPatente()   # solo la patente
            ))
            conn.commit()
            cursor.close()
            return "✅ Arriendo creado correctamente"
        except Exception as e:
            return f"❌ Error al insertar Arriendo: {str(e)}"

    @staticmethod
    def listarArriendos(conn):
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM arriendos"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()

            arriendos = []
            for resultado in resultados:
                cliente = Cliente(resultado[4])          # run_cliente
                empleado = Empleado(codigo=resultado[5]) # codigo_empleado
                vehiculo = Vehiculo(resultado[6])        # patente_vehiculo
                conversion = Conversion(fecha=resultado[1], costo=resultado[3])  # usar fecha_inicio como referencia

                arriendo = Arriendo(
                    num_arriendo=resultado[0],
                    fecha_inicio=resultado[1],
                    fecha_entrega=resultado[2],
                    costo_total=conversion,
                    cliente=cliente,
                    empleado=empleado,
                    vehiculo=vehiculo
                )
                arriendos.append(arriendo)
            return arriendos
        except Exception as e:
            print(f"❌ Error al listar arriendos: {str(e)}")
            return []
