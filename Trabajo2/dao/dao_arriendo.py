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
            sql = """
            SELECT 
                a.num_arriendo,
                a.fecha_inicio,
                a.fecha_entrega,
                a.costo_total_uf,

                c.run, c.nombre, c.apellido,
                e.codigo, e.nombre, e.apellido,
                v.patente, v.marca, v.modelo, v.precio
            FROM arriendos a
            JOIN clientes c ON a.run_cliente = c.run
            JOIN empleados e ON a.codigo_empleado = e.codigo
            JOIN vehiculos v ON a.patente_vehiculo = v.patente;
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()

            arriendos = []
            for r in resultados:

                cliente = Cliente(
                    run=r[4],
                    nombre=r[5],
                    apellido=r[6]
                )

                empleado = Empleado(
                    codigo=r[7],
                    nombre=r[8],
                    apellido=r[9]
                )

                vehiculo = Vehiculo(
                    patente=r[10],
                    marca=r[11],
                    modelo=r[12],
                    precio=r[13]
                )

                conversion = Conversion(
                    fecha=r[1],
                    costo=r[3]
                )

                arriendo = Arriendo(
                    num_arriendo=r[0],
                    fecha_inicio=r[1],
                    fecha_entrega=r[2],
                    costo_total=conversion,
                    cliente=cliente,
                    empleado=empleado,
                    vehiculo=vehiculo
                )

                arriendos.append(arriendo)

            return arriendos
        except Exception as e:
            print("❌ Error:", e)
            return []
