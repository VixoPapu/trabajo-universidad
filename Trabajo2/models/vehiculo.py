class Vehiculo:
    def __init__ (self, patente, marca, modelo, anio, precio, disponible, piezas, lista_vehiculo):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__precio = precio
        self.__disponible = disponible
        self.__piezas = piezas
        self.__lista_vehiculo = lista_vehiculo
        

    def get_patente(self):
        return self.__patente
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_anio(self):
        return self.__anio
    def get_precio(self):
        return self.__precio
    def get_disponible(self):
        return self.__disponible
    def get_piezas(self):
        return self.__piezas
    def get_lista_vehiculo(self):
        return self.__lista_vehiculo



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
    def set_piezas(self, piezas):
        self.__piezas = piezas
    def set_lista_vehiculo(self, lista_vehiculo):
        self.__lista_vehiculo = lista_vehiculo


    def mostrar_info(self):
        return f"Patente: {self.__patente}, Marca: {self.__marca}, Modelo: {self.__modelo}, Tipo: {self.__tipo}, Precio: {self.__precio}"
