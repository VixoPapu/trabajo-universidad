from models.vehiculo import Vehiculo



def agregar_vehiculo(self, vehiculo):
    cursor = self.conexion.cursor()
    sql = "INSERT INTO Vehiculos (patente, marca, modelo, anio, precio, disponible) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (
        Vehiculo.get_patente(),
        Vehiculo.get_marca(),
        Vehiculo.get_modelo(),
        Vehiculo.get_anio(),
        Vehiculo.get_precio(),
        Vehiculo.get_disponible()
    ))
    self.conexion.commit()