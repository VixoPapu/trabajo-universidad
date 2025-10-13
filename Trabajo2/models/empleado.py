# models/empleado.py

class Empleado:
    def __init__(self, codigo, run, nombre, apellido, cargo):
        self.codigo = codigo
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

