class Vehiculo:
    
    def __init__ (self, patente, marca, modelo, anio, precio, disponible):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__precio = precio
        self.__disponible = disponible

    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getAnio(self):
        return self.__anio
    def getPrecio(self):
        return self.__precio
    def getDisponible(self):
        return self.__disponible

    def set_patente(self, patente):
        self.__patente = patente
    def set_marca(self, marca):
        self.__marca = marca
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_anio(self, anio):
        self.__anio = anio
    def set_precio(self, precio):
        self.__precio = precio
    def set_disponible(self, disponible):
        self.__disponible = disponible

    def mostrar_info(self):
        return f"Patente: {self.__patente} | Marca: {self.__marca} | Modelo: {self.__modelo} | Año: {self.__anio} | Precio: ${self.__precio}"
