from models.persona import Persona

class Empleado(Persona):
    def __init__(self, codigo=None, cargo=None, password=None, run=None, nombre=None, apellido=None):
        self.__codigo = codigo
        self.__cargo = cargo
        self.__password = password
        super().__init__(run, nombre, apellido)


    def getCodigo(self):
        return self.__codigo
    def getCargo(self):
        return self.__cargo
    def getPassword(self):
        return self.__password

    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_password(self, password):
        self.__password = password
    
    def nombre_completo(self):
        return f"{self.getNombre()} {self.getApellido()}"
    def __str__(self):
        return f"{self.getCodigo()} | {self.nombre_completo()} | {self.__cargo} | Run: {self.getRun()}"

    @classmethod
    def from_login(cls, run, password):
        return cls(password=password, run=run)