from datetime import date

class Conversion:
    def __init__(self, fecha: date, costo: float):
        self.__fecha = fecha
        self.__costo = costo

    def getFecha(self):
        return self.__fecha

    def getCosto(self):
        return self.__costo

    def set_fecha(self, fecha: date):
        self.__fecha = fecha

    def set_costo(self, costo: float):
        self.__costo = costo

    def __str__(self):
        return f"Fecha: {self.__fecha} | Valor UF: {self.__costo}"
