import bcrypt
from models.empleado import Empleado

class EmpDAO:
    def validarLogin(conn, run, password):
        try:
            cur = conn.cursor()
            sql = "SELECT codigo, run, nombre, apellido, cargo, password FROM empleados WHERE run = %s LIMIT 1"
            cur.execute(sql, (run,))
            row = cur.fetchone()
            cur.close()

            if row:
                codigo, run, nombre, apellido, cargo, hashed_pw = row
                if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
                    return Empleado(codigo, cargo, hashed_pw, run, nombre, apellido)
            return None
        except Exception as ex:
            print("Error:", ex)
            return None

    def registrarEmpleado(conn, empleado):
        try:
            cur = conn.cursor()
            sql = "INSERT INTO empleados (run, nombre, apellido, cargo, password) VALUES (%s, %s, %s, %s, %s)"
            hashed_pw = bcrypt.hashpw(empleado.getPassword().encode(), bcrypt.gensalt()).decode()
            cur.execute(sql, (
                empleado.getRun(),
                empleado.getNombre(),
                empleado.getApellido(),
                empleado.getCargo(),
                hashed_pw
            ))
            conn.commit()
            cur.close()
            return "Empleado registrado correctamente"
        except Exception as e:
            print("Error al registrar empleado:", e)
            return "Error al registrar empleado"

    def listarEmpleados(conn):
        try:
            cur = conn.cursor()
            sql = "SELECT codigo, cargo, password, run, nombre, apellido FROM empleados"
            cur.execute(sql)
            filas = cur.fetchall()
            cur.close()

            empleados = []
            for f in filas:
                empleado = Empleado(f[0], f[1], f[2], f[3], f[4], f[5])
                empleados.append(empleado)

            return empleados
        
        except Exception as e:
            print("Error al listar empleados:", e)
            return []