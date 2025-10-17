class Arriendo:
    def __init__(self, num_arriendo, fecha_inicio, fecha_entrega, costo_total, run_cliente, codigo_empleado, patente_vehiculo):
        self.__numArriendo = num_arriendo
        self.__fechaInicio = fecha_inicio
        self.__fechaEntrega = fecha_entrega
        self.__costoTotal = costo_total
        self.__runCliente = run_cliente
        self.__codigoEmpleado = codigo_empleado
        self.__patenteVehiculo = patente_vehiculo

    def __str__(self):
        return f"Arriendo Nº{self.__numArriendo} - Cliente: {self.__runCliente} - Vehículo: {self.__patenteVehiculo} - Total: {self.__costoTotal}"