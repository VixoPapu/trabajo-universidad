# Hacer el DTO con las funciones del DAO
from dao.dao_empleado import EmpDAO

class EmpDTO:
    def validarLogin(self, conn, run, password):
        resultado = EmpDAO.validarLogin(conn, run, password)
        return resultado
    
    def registrarEmpleado(sefl, conn, empleado):
        return EmpDAO.registrarEmpleado(conn, empleado)

    def listarEmpleados(self, conn):
        return EmpDAO.listarEmpleados(conn)