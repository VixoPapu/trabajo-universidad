class Empleado:
    def __init__(self, codigo, cargo, password, run, nombre, apellido):
        self.__codigo = codigo
        self.__cargo = cargo
        self.__password = password
        self.__run = run
        self.__nombre = nombre
        self.__apellido = apellido

    def getCodigo(self):
        return self.__codigo
    def getCargo(self):
        return self.__cargo
    def getPassword(self):
        return self.__password
    def getRun(self):
        return self.__run
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} - {self.__cargo}"
