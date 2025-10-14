class Empleado:
    def __init__(self, codigo, cargo, password, run, nombre, apellido):
        self.__codigo = codigo
        self.__cargo = cargo
        self.__password = password
        self.__run = run
        self.__nombre = nombre
        self.__apellido = apellido

    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    def __str__(self):
        return f"{self.__nombre} {self.__apellido} - {self.__cargo}"