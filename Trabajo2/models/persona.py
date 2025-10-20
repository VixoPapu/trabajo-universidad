class Persona:
    def __init__(self, run, nombre, apellido):
        self.__run = run
        self.__nombre = nombre
        self.__apellido = apellido

    def getRun(self):
        return self.__run
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido