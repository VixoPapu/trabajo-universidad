from controlador.validations import login, registrar, mostrar_menu

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
            empleado = login()
            mostrar_menu(empleado)
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
