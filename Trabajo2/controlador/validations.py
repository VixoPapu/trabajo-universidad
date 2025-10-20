from models.empleado import Empleado
from getpass import getpass
from database.db_connection import Connex
from controlador.dto_empleado import EmpDTO

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
    mensaje = EmpDTO().registrarEmpleado(db.connection, empleado)
    print(mensaje)

    db.close()

def login():
    db = Connex()
    db.connect()

    print("-- Inicio de sesión --")
    run = input("RUN: ")
    password = getpass("Contraseña: ")

    empleado = EmpDTO().validarLogin(db.connection, run, password)

    if empleado:
        return empleado
    else:
        print("Credenciales incorrectas. Verifique los datos.")
        return None

def menu_principal():
    while True:
        print("-- Menu Principal --")
        print("")
        print("1. Iniciar Sesion")
        print("2. Registrar")
        print("3. Cerrar Programa")
        print("")
        
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            print("")
            print("Iniciando Sesion...")
            empleado = login()
            mostrar_menu(empleado)
        elif opc == "2":
            print("")
            print("Registrando Usuario...")
            registrar()
        elif opc == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida, intente de nuevo")


def mostrar_menu(empleado: Empleado):
    while True:
        print("\n" + "="*40)
        print(f"Bienvenido {empleado.nombre_completo()} Cargo: {empleado.getCargo().upper()}")
        print("")
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
            db = Connex()
            db.connect()

            empleados = EmpDTO().listarEmpleados(db.connection)
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print("")
                print("Lista de empleados:")
                for emp in empleados:
                    print(f"{emp.getCodigo()} | Nombre: {emp.nombre_completo()} | Cargo: {emp.getCargo()} | Run: {emp.getRun()}")
            db.close()
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
            
