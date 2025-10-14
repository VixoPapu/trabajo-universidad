from controlador.validations import mostrar_menu
from dao.dao_empleado import validar_empleado
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
        empleado = validar_empleado(db.connection, run, password)

        if not empleado:
            print("RUN o contraseña incorrectos. Intente nuevamente.\n")
            intentos += 1

    if empleado:
        mostrar_menu(empleado)
    else:
        print("Ha excedido el número de intentos. Saliendo del sistema.")

    db.close()

if __name__ == "__main__":
    login()