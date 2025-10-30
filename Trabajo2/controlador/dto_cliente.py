from dao.dao_cliente import ClienteDAO
from database.db_connection import Connex
from models.cliente import Cliente
class ClienteDTO:


    def insertar(self, run, nombre, apellido, telefono, direccion):
        db = Connex()
        db.connect()
        cliente = Cliente(run=run, nombre=nombre, apellido=apellido, telefono= telefono, direccion=direccion)
        resultado = ClienteDAO.insertar(db.connection, cliente)
        db.close()
        return resultado
    
    def editar(self, run, nombre, apellido, telefono, direccion):
        db = Connex()
        db.connect()
        cliente = Cliente(run=run, nombre=nombre, apellido=apellido, telefono= telefono, direccion=direccion)
        resultado = ClienteDAO.editar(db.connection, cliente)
        db.close()
        return resultado
    
    def eliminar(self, run):
        db = Connex()
        db.connect()
        cliente = Cliente(run=run)
        resultado = ClienteDAO.eliminar(db.connection, cliente)
        db.close()
        return resultado

    def mostrar(self, run):
        db = Connex()
        db.connect()
        cliente = Cliente(run=run)
        resultado = ClienteDAO.mostrar(db.connection, cliente)
        db.close()
        return resultado
    
    def listarClientes(self):
        db = Connex()
        db.connect()
        resultado = ClienteDAO.listarClientes(db.connection)
        db.close()
        return resultado