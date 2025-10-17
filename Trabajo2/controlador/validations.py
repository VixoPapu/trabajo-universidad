from models.empleado import Empleado
from getpass import getpass
from database.db_connection import Connex
from dao.dao_empleado import registrarEmpleado, validarLogin

def registrar():
    db = Connex()
    db.connect()

    print("-- Registro de usuario --")
    run = ""
    while len(run) < 9:
        run = input("Ingrese su rut: ")
        if len(run) < 9:
            print("El rut debe tener al menos 9 caracteres.")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo: ")
    password = getpass("Contraseña: ")
    password2 = getpass("Confirmar Contraseña: ")

    if password != password2:
        print("Las contraseñas no coinciden")
        db.close()
        return

    empleado = Empleado(None, cargo, password, run, nombre, apellido)
    mensaje = registrarEmpleado(db.connection, empleado)
    print(mensaje)

    db.close()

def login():
    db = Connex()
    db.connect()

    print("-- Inicio de sesión --")
    run = input("RUN: ")
    nombre = input("Nombre: ")
    password = getpass("Contraseña: ")

    empleado = validarLogin(db.connection, run, password)

    if empleado:
        print(f"Bienvenido {empleado.nombre_completo()}!")
        return empleado
    else:
        print("Credenciales incorrectas. Verifique los datos.")
        return None

def mostrar_menu(empleado: Empleado):
    while True:
        print("\n" + "="*40)
        print(f"Bienvenido {empleado.nombre_completo()} (cargo: {empleado.getCargo().upper()})")
        print("1) Gestión Clientes")
        print("2) Gestión Vehículos")
        print("3) Gestión Empleados")
        print("4) Cerrar sesión")
        print("="*40)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Accediendo a Gestión Clientes...")
        elif opcion == "2":
            print("Accediendo a Gestión Vehículos...")
        elif opcion == "3":
            print("Accediendo a Gestión Empleados...")
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
            