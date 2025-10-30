from models.persona import Persona

class Cliente(Persona):
    def __init__(self, run, nombre=None, apellido=None, telefono=None, direccion=None):
        super().__init__(run, nombre, apellido)
        self.__telefono = telefono
        self.__direccion = direccion
    
    def getTelefono(self):
        return self.__telefono
    def getDireccion(self):
        return self.__direccion
    
    def set_telefono(self, telefono):
        self.__telefono = telefono
    def set_Direccion(self, direccion):
        self.__direccion = direccion


    def __str__(self):
        return f"Run: {self.getRun()} | Cliente: {self.getNombre()} {self.getApellido()} | Tel: {self.getTelefono()} | Direccion: {self.getDireccion()}"