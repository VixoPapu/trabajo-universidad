from models.empleado import Empleado
#from dao.dao_empleado import registrarEmpleado
from dao.dao_empleado import validarLogin
from database.db_connection import Connex
from getpass import getpass

def login():
    db = Connex()
    db.connect()
    
    empleado = None
    intentos = 0
    while not empleado and intentos < 3:
        run = input("Ingrese su RUN: ")
        password = getpass("Ingrese su contraseña: ")
        empleado = validarLogin(db.connection, run, password)

        if not empleado:
            print("RUN o contraseña incorrectos. Intente nuevamente.\n")
            intentos += 1

    if empleado:
        mostrar_menu(empleado)
    else:
        print("Ha excedido el número de intentos. Saliendo del sistema.")

    db.close()


def mostrar_menu(empleado: Empleado):
    while True:
        print("\n" + "="*40)
        print(f"Bienvenido {empleado.nombre_completo()} (cargo: {empleado.getCargo()})")
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