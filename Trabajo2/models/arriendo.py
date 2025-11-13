from datetime import date
from models.conversion import Conversion
from models.cliente import Cliente
from models.empleado import Empleado
from models.vehiculo import Vehiculo

class Arriendo:
    def __init__(self, num_arriendo: int, fecha_inicio: date, fecha_entrega: date,
                 costo_total: Conversion, cliente: Cliente, empleado: Empleado, vehiculo: Vehiculo):
        self.__num_arriendo = num_arriendo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_entrega = fecha_entrega
        self.__costo_total = costo_total
        self.__cliente = cliente
        self.__empleado = empleado
        self.__vehiculo = vehiculo
        self.__arriendos = []

    def getNumArriendo(self):
        return self.__num_arriendo

    def getFechaInicio(self):
        return self.__fecha_inicio

    def getFechaEntrega(self):
        return self.__fecha_entrega

    def getCostoTotal(self):
        return self.__costo_total

    def getCliente(self):
        return self.__cliente

    def getEmpleado(self):
        return self.__empleado

    def getVehiculo(self):
        return self.__vehiculo

    def getArriendos(self):
        return self.__arriendos

    def set_num_arriendo(self, num_arriendo):
        self.__num_arriendo = num_arriendo

    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def set_fecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = fecha_entrega

    def set_costo_total(self, conversion):
        self.__costo_total = conversion

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_empleado(self, empleado):
        self.__empleado = empleado

    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    def agregar_arriendo(self, arriendo):
        self.__arriendos.append(arriendo)

    def __str__(self):
        return (f"Arriendo Nº {self.__num_arriendo} | Inicio: {self.__fecha_inicio} | Entrega: {self.__fecha_entrega}\n"
                f"Cliente: {self.__cliente.getNombre()} {self.__cliente.getApellido()} | "
                f"Empleado: {self.__empleado.getNombre()} {self.__empleado.getApellido()}\n"
                f"Vehículo: {self.__vehiculo.getMarca()} {self.__vehiculo.getModelo()} ({self.__vehiculo.getPatente()})\n"
                f"Costo total: UF {self.__vehiculo.getPrecio()} | Valor UF: {self.__costo_total.getCosto()} ({self.__costo_total.getFecha()})")
