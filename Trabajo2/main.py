from controlador.validations import login
from dao.dao_empleado import registrarEmpleado
from database.db_connection import Connex
from models.empleado import Empleado
from getpass import getpass

def registrar():
    db = Connex()
    db.connect()

    print("=== Registro de Nuevo Empleado ===")
    run = input("RUN: ")
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
            print("Iniciando Sesion...")
            login()
        elif opc == "2":
            print("Registrando Usuario...")
            registrar()
        elif opc == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida, intente de nuevo")

if __name__ == "__main__":
    menu_principal()
