from models.vehiculo import Vehiculo

def agregar_vehiculo(self, vehiculo): #mati si haces self, vehiculo recuerda llamarlo despues 
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