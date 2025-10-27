from dao.dao_empleado import EmpDAO
from database.db_connection import Connex
from models.empleado import Empleado

class EmpDTO:
    def validarLogin(self, run, password):
        empleado_login = Empleado.from_login(run, password)
        db = Connex()
        db.connect()
        
        resultado = EmpDAO.validarLogin(db.connection, empleado_login)  
        db.close()
        return resultado
    
    def registrarEmpleado(self, cargo, password, run, nombre, apellido):
        empleado = Empleado(cargo=cargo, password=password, run=run, nombre=nombre, apellido=apellido)
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
    

    