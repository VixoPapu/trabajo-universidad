from dao.dao_cliente import ClienteDAO
from models.cliente import Cliente

class ClienteDTO:
    def __init__(self):
        self.dao = ClienteDAO()
    
    def insertarCliente(self, run, nombre, apellido, telefono, direccion):
        cliente = Cliente(run, nombre, apellido, telefono, direccion)
        return self.dao.insertar(cliente)
    
    def editarCliente(self, run, nombre, apellido, telefono, direccion):
        cliente = Cliente(run, nombre, apellido, telefono, direccion)
        return self.dao.editar(cliente)
    
    def eliminarCliente(self, run):
        return self.dao.eliminar(run)
    
    def mostrarCliente(self, run):
        return self.dao.mostrar(run)
    
    def listarClientes(self):
        return self.dao.listar_clientes()
    
    def existeCliente(self, run):
        return self.dao.mostrar(run) is not None