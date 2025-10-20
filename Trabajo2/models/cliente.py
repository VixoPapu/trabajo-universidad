from models.persona import Persona

class Cliente(Persona):
    def __init__(self, run, nombre, apellido, telefono, direccion):
        super().__init__(run, nombre, apellido)
        self.__telefono = telefono
        self.__direccion = direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getDireccion(self):
        return self.__direccion
    
    def __str__(self):
        return f"Cliente: {self.getNombre()} {self.getApellido()} | Tel: {self.__telefono}"