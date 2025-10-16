import bcrypt
from models.empleado import Empleado

def registrarEmpleado(conn, empleado):
    try:
        cur = conn.cursor()
        sql = "INSERT INTO empleados (run, nombre, apellido, cargo, password) VALUES (%s, %s, %s, %s, %s)"
        hashed_pw = bcrypt.hashpw(empleado._Empleado__password.encode(), bcrypt.gensalt()).decode()
        cur.execute(sql, (
            empleado._Empleado__run,
            empleado._Empleado__nombre,
            empleado._Empleado__apellido,
            empleado._Empleado__cargo,
            hashed_pw
        ))
        conn.commit()
        cur.close()
        return "Empleado registrado"
    except Exception as e:
        print("Error al registrar empleado:", e)
        return "Error al registrar empleado"

def validarLogin(conn, run, password):
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