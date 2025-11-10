from models.empleado import Empleado
from models.vehiculo import Vehiculo
from models.cliente import Cliente
from models.arriendo import Arriendo
from getpass import getpass
from database.db_connection import Connex
from controlador.dto_empleado import EmpDTO
from controlador.dto_cliente import ClienteDTO
from controlador.dto_vehiculo import VehiculoDTO
from controlador.dto_arriendo import ArriendoDTO
from getpass import getpass

def pedir_input(mensaje, minimo, campo=""):
    while True:
        valor = input(mensaje).strip()
        if len(valor) >= minimo:
            return valor
        print(f"El {campo or 'campo'} debe tener al menos {minimo} caracteres")

def registrar():
    db = Connex()
    db.connect()

    print("-- Registro de usuario --")
    run = pedir_input("Ingrese su Run: ", 9, "run")
    nombre = pedir_input("Nombre: ", 3, "nombre")
    apellido = pedir_input("Apellido: ", 3, "apellido")
    cargo = input("Cargo: ")

    password = getpass("Contraseña: ")
    password2 = getpass("Confirmar contraseña: ")

    if password != password2:
        print("Las contraseñas no coinciden")
        db.close()
        return

    mensaje = EmpDTO().registrarEmpleado(cargo, password, run, nombre, apellido)
    print(f"{mensaje}")

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
        print("2) Cerrar Programa")
        print("\n" + "="*40)
        
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            print("")
            print("Iniciando Sesion...")
            empleado = login()
            if empleado:
                mostrar_menu(empleado)

        elif opc == "2":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida, intente de nuevo")

def menu_gestion_vehiculos(vehiculo: Vehiculo):
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
            marca = input(f"Marca [{vehiculo.getMarca()}]: ") or vehiculo.getMarca()
            modelo = input(f"Modelo [{vehiculo.getModelo()}]: ") or vehiculo.getModelo()
            anio = input(f"Año [{vehiculo.getAnio()}]: ") or vehiculo.getAnio()
            precio = input(f"Precio [{vehiculo.getPrecio()}]: ") or vehiculo.getPrecio()
            estado_actual = "Si" if vehiculo.getDisponible() == 1 else "No"
            disponible_input = input(f"Disponible (sí/no) [{estado_actual}]: ").strip().lower()

            if disponible_input == "":
                disponible = vehiculo.getDisponible()  # mantiene valor actual
            elif disponible_input in ["si", "sí", "1", "true"]:
                disponible = 1
            elif disponible_input in ["no", "0", "false"]:
                disponible = 0
            else:
                print("Opcion invalida")
                disponible = vehiculo.getDisponible()


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

def menu_gestion_cliente(cliente: Cliente):
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
            run = pedir_input("Ingrese el Run: ", 9, "run")
            nombre = pedir_input("Ingrese el Nombre: ", 3, "nombre")
            apellido = pedir_input("Ingrese el Apellido: ", 3, "Apellido")
            telefono = pedir_input("Ingrese el Telefono: ", 9, "Telefono")
            direccion = input("Ingrese el direccion: ")

#Hice el cambio aqui llamando todo del dto_cliente

            #cliente = Cliente(run, nombre, apellido, telefono, direccion) <---antes
            resultado = ClienteDTO().insertar(run, nombre, apellido, telefono, direccion) #<----despues
            print(resultado)

        elif opcion == "2":
            print("\n--- Editando Cliente ---")
            run = input("Inserte el rut del cliente a editar: ")
            print("Editando el cliente con el rut", run)
            run = input(f"Run [{cliente.getRun()}]: ") or cliente.getRun()
            nombre = input(f"Nombre [{cliente.getNombre()}]: ") or cliente.getNombre()
            apellido = input(f"Apellido [{cliente.getApellido()}]: ") or cliente.getApellido()
            telefono = input(f"Teléfono [{cliente.getTelefono()}]: ") or cliente.getTelefono()
            direccion = input(f"Dirección [{cliente.getDireccion()}]: ") or cliente.getDireccion()

            resultado = ClienteDTO().editar(run, nombre, apellido, telefono, direccion)
            print(cliente)

        elif opcion == "3":
            print("\n--- Eliminando Cliente ---")
            run = input("Inserte el rut del cliente a eliminar: ")
            confirmar = input(f"¿Está seguro de eliminar el cliente {run}? (s/n): ")
            if confirmar.lower() == "s":
                resultado = ClienteDTO().eliminar(run)
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

def menu_empleado(empleado: Empleado):
    while True:
        print("\n" + "="*40)
        print("")
        print("1) Registrar Empleado")
        print("2) Listar Empleado")
        print("3) Volver al menu")
        print("\n" + "="*40)

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print("\n--- Registrando Empleado ---")
            registrar()

        elif opcion == "2":
            print("\n--- Lista de Empleado ---")
            empleados = EmpDTO().listarEmpleados()  
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print("")
                print("Lista de empleados: ")
                print("\n" + "="*40)
                for emp in empleados:
                    print(emp)
        elif opcion == "3":
            break

            
def menu_Arriendo(arriendo: Arriendo):
    while True:
        print("\n" + "="*40)
        print("")
        print("1) Registrar Arriendo")
        print("2) Listar Arriendo")
        print("\n" + "="*40)

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print("\n--- Ingresando Arriendo ---")
            num_arriendo = input("Ingresar numero de arriendo: ")
            fecha_inicio = ("Ingresar fecha de inicio: ")
            fecha_entrega = input("Ingresar fecha de entrega: ")
            costo_total= input("Ingresar costo total: ")
            cliente = input("Ingresar cliente: ")
            empleado = input("Ingresar empleado: ")
            vehiculo = input("Ingresa vehiculo: ")
            #Terminar clase arriendo como corresponde
            resultado = ArriendoDTO().IngresarArriendo(num_arriendo, fecha_inicio, fecha_entrega, costo_total, cliente, empleado, vehiculo) #<----despues
            print(resultado)

        elif opcion == "2":
            print("\n--- Listando Arriendos ---")
            arriendo = ArriendoDTO().listarArriendo()  
            if not arriendo:
                print("No hay arriendos registrados.")
            else:
                print("")
                print("Lista de arriendo: ")
                print("\n" + "="*40)
                for arr in arriendo:
                    print(arr)
        
def mostrar_menu(empleado: Empleado):
    while True:
        print("\n" + "="*40)
        print(f"Bienvenido {empleado.nombre_completo()} Cargo: {empleado.getCargo().upper()}")
        print("")
        print("1) Gestión Clientes")
        print("2) Gestión Vehículos")
        print("3) Gestión Empleados")
        print("4) Gestión Arriendos")
        print("5) Cerrar sesión")
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
            menu_empleado(EmpDTO())

        elif opcion == "4":
            print("Accediendo a Gestión Arriendos")
            menu_Arriendo(ArriendoDTO())
            
        elif opcion == "5":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
    
