from models.empleado import Empleado

def mostrar_menu(empleado: Empleado):
    while True:
        print("\n" + "="*40)
        print(f"Bienvenido {empleado.nombre_completo()} (cargo: {empleado.cargo})")
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