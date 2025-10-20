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

def eliminar_vehiculo(self, vehiculo):
    cursor = self.conexion.cursor()
    sql = "DELETE FROM vehiculos WHERE patente = ?"
    cursor.execute(sql, (vehiculo.getPatente(),))
    self.conexion.commit()

def actualizar_vehiculo(self, vehiculo):
    cursor = self.conexion.cursor
    sql = ""
    cursor.execute(sql,(
        vehiculo.getPatente(),
        vehiculo.getMarca(),
        vehiculo.getModelo(),
        vehiculo.getAnio(),
        vehiculo.getPrecio(),
        vehiculo.getDisponible()
    ))
