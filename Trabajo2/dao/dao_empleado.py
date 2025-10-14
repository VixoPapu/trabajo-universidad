import bcrypt
from models.empleado import Empleado

def validar_empleado(conn, run, password):
    try:
        cur = conn.cursor()
        sql = "SELECT codigo, cargo, password, run, nombre, apellido FROM empleados WHERE run = %s LIMIT 1"
        cur.execute(sql, (run,))
        row = cur.fetchone()
        cur.close()

        if row:
            codigo, cargo, password_hashed, run_db, nombre, apellido = row
            if bcrypt.checkpw(password.encode(), password_hashed.encode()):
                return Empleado(codigo, cargo, password_hashed, run_db, nombre, apellido)
        return None
    except Exception as e:
        print("Error en la consulta de validación:", e)
        return None