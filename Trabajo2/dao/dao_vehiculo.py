from models.vehiculo import Vehiculo



def agregar_vehiculo(self, vehiculo):
    cursor = self.conexion.cursor()
    sql = "INSERT INTO Vehiculos (patente, marca, modelo, anio, precio, disponible) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (
        Vehiculo.getPatente(),
        Vehiculo.getMarca(),
        Vehiculo.getModelo(),
        Vehiculo.getAnio(),
        Vehiculo.getPrecio(),
        Vehiculo.getDisponible()
    ))
    self.conexion.commit()