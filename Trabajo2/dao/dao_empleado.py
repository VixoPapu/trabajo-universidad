import bcrypt
from models.empleado import Empleado

def validar_empleado(conn, run, password_plain):
    try:
        cur = conn.cursor()
        sql = "SELECT codigo, run, nombre, apellido, cargo, password FROM empleados WHERE run = %s LIMIT 1"
        cur.execute(sql, (run,))
        row = cur.fetchone()
        cur.close()

        if row:
            codigo, run_db, nombre, apellido, cargo, password_hashed = row
            if bcrypt.checkpw(password_plain.encode(), password_hashed.encode()):
                return Empleado(codigo, run_db, nombre, apellido, cargo)
        return None
    except Exception as e:
        print("Error en la consulta de validación:", e)
        return None