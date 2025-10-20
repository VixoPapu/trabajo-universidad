from models.empleado import Empleado
from getpass import getpass
from database.db_connection import Connex
from controlador.dto_empleado import EmpDTO
from controlador.dto_cliente import ClienteDTO
from controlador.dto_vehiculo import VehiculoDTO

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
  
    mensaje = EmpDTO().registrarEmpleado(cargo, password, run, nombre, apellido)
    print(mensaje)

    db.close()

def login():
    db = Connex()
    db.connect()

    print("-- Inicio de sesión --")
    run = input("RUN: ")
    password = getpass("Contraseña: ")
    resultado = EmpDTO().validarLogin(run, password)
    db.close()
    return resultado

def menu_principal():
    while True:
        print("\n" + "="*40)
        print("-- Menu Principal --")
        print("")
        print("1) Iniciar Sesion")
        print("2) Registrar")
        print("3) Cerrar Programa")
        print("\n" + "="*40)
        
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            print("")
            print("Iniciando Sesion...")
            empleado = login()
            if empleado:
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

def menu_gestion_vehiculos(vehiculo_dto):
    while True:
        print("\n" + "="*40)
        print("\n--- Gestión de Vehículos ---")
        print("")
        print("1) Modificar vehículo")
        print("2) Eliminar vehículo")
        print("3) Listar vehículos disponibles")
        print("4) Volver al menú anterior")
        print("\n" + "="*40)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Modificar Vehículo ---")
            patente = input("Patente: ")
            print("Modificando el auto con la patente", patente)
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = int(input("Año: "))
            precio = float(input("Precio: "))
            disponible = input("Disponible (si/no): ").lower() == "si"


            from models.vehiculo import Vehiculo
            vehiculo = Vehiculo(patente, marca, modelo, anio, precio, disponible)
            resultado = vehiculo_dto.modificar(vehiculo)
            print(resultado)

        elif opcion == "2":
            print("\n--- Eliminar Vehículo ---")
            patente = input("Patente del vehículo a eliminar: ")
            confirmar = input(f"¿Está seguro de eliminar el vehículo {patente}? (s/n): ")
            if confirmar.lower() == 's':
                resultado = vehiculo_dto.eliminar(patente)
                print(resultado)

        elif opcion == "3":
            print("\n--- Vehículos Disponibles ---")
            vehiculos = vehiculo_dto.listarDisponibilidad()
            if vehiculos:
                for vehiculo in vehiculos:
                    print("\n" + "="*40)
                    print(vehiculo.mostrar_info())

            else:
                print("No hay vehículos disponibles")

        elif opcion == "4":
            break
        else:
            print("Opción no válida")

def mostrar_menu(empleado: Empleado):
    vehiculo_dto = VehiculoDTO()
    while True:
        print("\n" + "="*40)
        print(f"Bienvenido {empleado.nombre_completo()} Cargo: {empleado.getCargo().upper()}")
        print("")
        print("1) Gestión Clientes")
        print("2) Gestión Vehículos")
        print("3) Gestión Empleados")
        print("4) Cerrar sesión")
        print("\n" + "="*40)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Accediendo a Gestión Clientes...")


        elif opcion == "2":
            print("Accediendo a Gestión Vehículos...")
            menu_gestion_vehiculos(vehiculo_dto)

        elif opcion == "3":
            print("Accediendo a Gestión Empleados...")
            
            empleados = EmpDTO().listarEmpleados()  
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print("")
                print("Lista de empleados:")
                for emp in empleados:
                    print(f"{emp.getCodigo()} | Nombre: {emp.nombre_completo()} | Cargo: {emp.getCargo()} | Run: {emp.getRun()}")
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
    
