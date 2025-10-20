from models.cliente import Cliente

class ClienteDAO:
    def insertar(self, cliente):
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO clientes (run, nombre, apellido, telefono, direccion) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                cliente.getRun(),
                cliente.getNombre(),
                cliente.getApellido(),
                cliente.getTelefono(),
                cliente.getDireccion()
            ))
            self.conexion.commit()
            cursor.close()
            return "Cliente insertado correctamente"
        except Exception as e:
            return f"Error al insertar cliente: {str(e)}"
    
    def editar(self, cliente):
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE clientes SET nombre=%s, apellido=%s, telefono=%s, direccion=%s WHERE run=%s"
            cursor.execute(sql, (
                cliente.getNombre(),
                cliente.getApellido(),
                cliente.getTelefono(),
                cliente.getDireccion(),
                cliente.getRun()
            ))
            self.conexion.commit()
            cursor.close()
            return "Cliente actualizado correctamente"
        except Exception as e:
            return f"Error al actualizar cliente: {str(e)}"
    
    def eliminar(self, run):
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM clientes WHERE run = %s"
            cursor.execute(sql, (run,))
            self.conexion.commit()
            cursor.close()
            return "Cliente eliminado correctamente"
        except Exception as e:
            return f"Error al eliminar cliente: {str(e)}"
    
    def mostrar(self, run):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM clientes WHERE run = %s"
            cursor.execute(sql, (run,))
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return Cliente(
                    run=resultado[0],
                    nombre=resultado[1],
                    apellido=resultado[2],
                    telefono=resultado[3],
                    direccion=resultado[4]
                )
            return None
        except Exception as e:
            print(f"Error al buscar cliente: {str(e)}")
            return None
    
    def listarClientes(self):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM clientes"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            
            clientes = []
            for resultado in resultados:
                cliente = Cliente(
                    run=resultado[0],
                    nombre=resultado[1],
                    apellido=resultado[2],
                    telefono=resultado[3],
                    direccion=resultado[4]
                )
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error al listar clientes: {str(e)}")
            return []