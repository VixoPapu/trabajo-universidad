class Arriendo:
    def __init__(self, num_arriendo, fecha_inicio, fecha_entrega, costo_total, cliente, empleado, vehiculo, arriendos):
        self.__numArriendo = num_arriendo
        self.__fechaInicio = fecha_inicio
        self.__fechaEntrega = fecha_entrega
        self.__costoTotal = costo_total
        self.__cliente = cliente
        self.__empleado = empleado
        self.__vehiculo = vehiculo
        self.__arriendos = arriendos

    def getNumArriendo(self):
        return self.__numArriendo
    def getFechaInicio(self):
        return self.__fechaInicio
    def getFechaEntrega(self):
        return self.__fechaEntrega
    def getCostoTotal(self):
        return self.__costoTotal
    def getCliente(self):
        return self.__cliente
    def getEmpleado(self):
        return self.__empleado
    def getVehiculo(self):
        return self.__vehiculo

    def __str__(self):
        return f"Arriendo Nº{self.__numArriendo} | Cliente: {self.__cliente} | Vehículo: {self.__vehiculo} | Total: {self.__costoTotal}"
