from dao.dao_cliente import ClienteDAO
from database.db_connection import Connex

class ClienteDTO:
    def insertar(self, cliente):
        db = Connex()
        db.connect()
        resultado = ClienteDAO.insertar(db.connection, cliente)
        db.close()
        return resultado
    
    def editar(self, cliente):
        db = Connex()
        db.connect()
        resultado = ClienteDAO.editar(db.connection, cliente)
        db.close()
        return resultado
    
    def eliminar(self, run):
        db = Connex()
        db.connect()
        resultado = ClienteDAO.eliminar(db.connection, run)
        db.close()
        return resultado
    
    def mostrar(self, run):
        db = Connex()
        db.connect()
        resultado = ClienteDAO.mostrar(db.connection, run)
        db.close()
        return resultado
    
    def listarClientes(self):
        db = Connex()
        db.connect()
        resultado = ClienteDAO.listarClientes(db.connection)
        db.close()
        return resultado