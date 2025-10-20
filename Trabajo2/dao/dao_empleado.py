import bcrypt
from models.empleado import Empleado

class EmpDAO:
    @staticmethod
    def validarLogin(conn, empleado):
        try:
            cur = conn.cursor()
            sql = "SELECT codigo, run, nombre, apellido, cargo, password FROM empleados WHERE run = %s LIMIT 1"
            cur.execute(sql, (empleado.getRun(),))
            row = cur.fetchone()
            cur.close()

            if row:
                codigo, run, nombre, apellido, cargo, hashed_pw = row
                if bcrypt.checkpw(empleado.getPassword().encode(), hashed_pw.encode()):
                    return Empleado(
                        codigo=codigo,
                        cargo=cargo,
                        password=hashed_pw,
                        run=run,
                        nombre=nombre,
                        apellido=apellido
                    )
            return None
        except Exception as ex:
            print("Error:", ex)
            return None

    @staticmethod
    def registrarEmpleado(conn, empleado: Empleado):
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
        
    @staticmethod
    def listarEmpleados(conn):
        try:
            cur = conn.cursor()
            sql = "SELECT codigo, cargo, password, run, nombre, apellido FROM empleados"
            cur.execute(sql)
            filas = cur.fetchall()
            cur.close()

            empleados = []
            for f in filas:
                empleado = Empleado(
                    codigo=f[0],
                    cargo=f[1],
                    password=f[2],
                    run=f[3],
                    nombre=f[4],
                    apellido=f[5],
                )
                empleados.append(empleado)

            return empleados if empleados else []
        
        except Exception as e:
            print("Error al listar empleados:", e)
            return []