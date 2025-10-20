from models.vehiculo import Vehiculo

class VehiculoDAO:
    @staticmethod
    def modificar(conn, vehiculo):
        try:
            cursor = conn.cursor()
            sql = """UPDATE vehiculos SET marca=%s, modelo=%s, anio=%s, 
                     precio=%s, disponible=%s WHERE patente=%s"""
            cursor.execute(sql, (
                vehiculo.getMarca(),
                vehiculo.getModelo(),
                vehiculo.getAnio(),
                vehiculo.getPrecio(),
                vehiculo.getDisponible(),
                vehiculo.getPatente()
            ))
            conn.commit()
            cursor.close()
            return "Vehículo modificado correctamente"
        except Exception as e:
            return f"Error al modificar vehículo: {str(e)}"
        
    @staticmethod
    def eliminar(conn, patente):
        """Elimina un vehículo por patente - Requirement: +eliminar(patente): string"""
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM vehiculos WHERE patente = %s"
            cursor.execute(sql, (patente,))
            conn.commit()
            cursor.close()
            return "Vehículo eliminado correctamente"
        except Exception as e:
            return f"Error al eliminar vehículo: {str(e)}"
        
    @staticmethod
    def listarDisponibilidad(conn):
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM vehiculos WHERE disponible = TRUE"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            
            vehiculos = []
            for resultado in resultados:
                vehiculos.append(Vehiculo(
                    patente=resultado[0],
                    marca=resultado[1], 
                    modelo=resultado[2],
                    anio=resultado[3],
                    precio=resultado[4],
                    disponible=resultado[5]
                ))

            return vehiculos
        except Exception as e:
            print(f"Error al listar vehículos disponibles: {str(e)}")
            return []
