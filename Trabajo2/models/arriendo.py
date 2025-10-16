class Arriendo:
    def __init__(self, num_arriendo, fecha_inicio, fecha_entrega, costo_total, run_cliente, codigo_empleado, patente_vehiculo):
        self.__num_arriendo = num_arriendo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_entrega = fecha_entrega
        self.__costo_total = costo_total
        self.__run_cliente = run_cliente
        self.__codigo_empleado = codigo_empleado
        self.__patente_vehiculo = patente_vehiculo

    def __str__(self):
        return f"Arriendo Nº{self.__num_arriendo} - Cliente: {self.__run_cliente} - Vehículo: {self.__patente_vehiculo} - Total: {self.__costo_total}"