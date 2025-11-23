class Persona:
    def __init__(self, run, nombre, apellido):
        self._run = run
        self._nombre = nombre
        self._apellido = apellido
    
    def getRun(self):
        return self._run
    def getNombre(self):
        return self._nombre
    def getApellido(self):
        return self._apellido

    def set_Nombre(self, nombre):
        self._nombre = nombre
    def set_Apellido(self, apellido):
        self._apellido = apellido

    def __str__(self):
        return f"{self._nombre} {self._apellido} | Run: {self._run})"