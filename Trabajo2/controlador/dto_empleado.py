from dao.dao_empleado import EmpDAO
from database.db_connection import Connex
from models.empleado import Empleado

class EmpDTO:
    def validarLogin(self, run, password):
        empleado = Empleado(None, None, password, run, None, None)
        db = Connex()
        db.connect()
        resultado = EmpDAO.validarLogin(db.connection, empleado)  
        db.close()
        return resultado
    
    def registrarEmpleado(self, cargo, password, run, nombre, apellido):
        empleado = Empleado(None, cargo, password, run, nombre, apellido)
        db = Connex()
        db.connect()
        resultado = EmpDAO.registrarEmpleado(db.connection, empleado) 
        db.close()
        return resultado

    def listarEmpleados(self):
        db = Connex()
        db.connect()
        resultado = EmpDAO.listarEmpleados(db.connection) 
        db.close()
        return resultado