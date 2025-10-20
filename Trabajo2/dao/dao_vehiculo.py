from models.vehiculo import Vehiculo

class VehiculoDAO:
    def agregar_vehiculo(self, vehiculo):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO Vehiculos (patente, marca, modelo, anio, precio, disponible) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            vehiculo.getPatente(),
            vehiculo.getMarca(),
            vehiculo.getModelo(),
            vehiculo.getAnio(),
            vehiculo.getPrecio(),
            vehiculo.getDisponible()
        ))
        self.conexion.commit()