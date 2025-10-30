from models.empleado import Empleado
from models.vehiculo import Vehiculo
from models.cliente import Cliente 
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
            patente = input("Patente de vehiculo a modificar: ")
            print("Modificando el auto con la patente", patente)
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = int(input("Año: "))
            precio = float(input("Precio: "))
            disponible = input("Disponible (si/no): ").lower() == "si"

           #CAMBIO aca
            resultado = VehiculoDTO().modificar(patente, marca, modelo, anio, precio, disponible)
            print(resultado)

        elif opcion == "2":
            print("\n--- Eliminar Vehículo ---")
            patente = input("Patente del vehículo a eliminar: ")
            confirmar = input(f"¿Está seguro de eliminar el vehículo {patente}? (s/n): ")
            if confirmar.lower() == 's':
                resultado = VehiculoDTO().eliminar(patente)
                print(resultado)

        elif opcion == "3":
            print("\n--- Vehículos Disponibles ---")
            vehiculos = VehiculoDTO().listarDisponibilidad()
            print("\n" + "="*40)
            if vehiculos:
                for vehiculo in vehiculos:
                    print(vehiculo)

            else:
                print("No hay vehículos disponibles")

        elif opcion == "4":
            break
        else:
            print("Opción no válida")

def menu_gestion_cliente(cliente_dto):
    while True:
        print("\n" + "="*40)
        print("")
        print("1) Insertar Cliente")
        print("2) Editar Cliente")
        print("3) Eliminar Cliente")
        print("4) Mostrar Cliente")
        print("5) Listar Clientes")
        print("6) Volver al menú anterior")
        print("\n" + "="*40)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("\n--- Insertando Cliente ---")
            run = input("Ingrese el rut: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            telefono = input("Ingrese el telefono: ")
            direccion = input("Ingrese el direccion: ")

#Hice el cambio aqui llamando todo del dto_cliente

            #cliente = Cliente(run, nombre, apellido, telefono, direccion) <---antes
            resultado = ClienteDTO().insertar(run, nombre, apellido, telefono, direccion) #<----despues
            print(resultado)

        elif opcion == "2":
            print("\n--- Editando Cliente ---")
            run = input("Inserte el rut del cliente a editar: ")
            print("Editando el cliente con el rut", run)
            nombre = input("Ingrese nuevo nombre: ")
            apellido = input("Ingrese nuevo apellido: ")
            telefono = input("Ingrese nuevo telefono: ")
            direccion = input("Ingrese nueva direccion: ")

            #cliente = Cliente(run, nombre, apellido, telefono, direccion)
            resultado = ClienteDTO().editar(run, nombre, apellido, telefono, direccion)
            print(cliente)

        elif opcion == "3":
            print("\n--- Eliminando Cliente ---")
            run = input("Inserte el rut del cliente a eliminar")
            confirmar = input(f"¿Está seguro de eliminar el cliente {run}? (s/n): ")
            if confirmar.lower() == "s":
                resultado = ClienteDTO().eliminar(run)
                print("Cliente elimiado con exito...")
                print(resultado)

        elif opcion == "4":
            print("\n--- Mostrando Cliente ---")
            run = input("Inserte el rut del cliente a mostrar: ")
            resultado = ClienteDTO().mostrar(run)
            print(resultado)

        elif opcion == "5":
            print("\n--- Listando Clientes ---")
            clientes = ClienteDTO().listarClientes()
            print("\n" + "="*40)
            if clientes:
                for cliente in clientes:
                    print(cliente)

        elif opcion == "6":
            break

        else:
            print("Opción inválida, intente nuevamente.")

def mostrar_menu(empleado: Empleado):
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
            menu_gestion_cliente(ClienteDTO())

        elif opcion == "2":
            print("Accediendo a Gestión Vehículos...")
            menu_gestion_vehiculos(VehiculoDTO())

        elif opcion == "3":
            print("Accediendo a Gestión Empleados...")
            
            empleados = EmpDTO().listarEmpleados()  
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print("")
                print("Lista de empleados: ")
                print("\n" + "="*40)
                for emp in empleados:
                    print(emp)

        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
    
