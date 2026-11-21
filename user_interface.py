import os

from business_logic import CadenaHotelera, Hotel, validar_dias_a_simular


def limpiar_consola() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mostrar_menu() -> None:
    print("========== CADENA SOL CARIBE ==========")
    print("1. Crear un hotel")
    print("2. Registrar las habitaciones ocupadas del día siguiente")
    print("3. Simular días")
    print("4. Ver el informe de un hotel")
    print("7. Salir")


def pedir_hotel(cadena: CadenaHotelera) -> Hotel | None:
    nombre = input("Nombre del hotel: ")
    hotel = cadena.buscar_hotel(nombre)
    if hotel is None:
        print("No hay un hotel con ese nombre.")
    return hotel


def opcion_crear_hotel(cadena: CadenaHotelera) -> None:
    nombre = input("Nombre del hotel: ")
    habitaciones = input("Habitaciones habilitadas: ")
    anio = input("Año de inicio del registro: ")
    mes = input("Mes de inicio: ")
    dia = input("Día de inicio: ")
    mensaje = cadena.crear_hotel(nombre, habitaciones, anio, mes, dia)
    if mensaje == "":
        print(f"Se creó el hotel {nombre.strip()}, sin días registrados.")
    else:
        print(mensaje)


def opcion_registrar_dia(cadena: CadenaHotelera) -> None:
    hotel = pedir_hotel(cadena)
    if hotel is not None:
        fecha = hotel.fecha_siguiente()
        print(f"Día siguiente del registro: {fecha}")
        registrado = False
        while not registrado:
            try:
                cantidad = int(input(f"Habitaciones ocupadas del {fecha}: "))
                mensaje = hotel.validar_ocupadas(cantidad)
                if mensaje == "":
                    hotel.registrar_dia(cantidad)
                    registrado = True
                    print(f"Se registró el día {fecha}.")
                else:
                    print(mensaje)
            except ValueError:
                print("Las habitaciones ocupadas deben ser un número entero.")


def opcion_simular_dias(cadena: CadenaHotelera) -> None:
    hotel = pedir_hotel(cadena)
    if hotel is not None:
        seguir = True
        dias = 0
        minimo = 0
        maximo = 0

        try:
            dias = int(input("Número de días a simular: "))
            mensaje = validar_dias_a_simular(dias)
        except ValueError:
            mensaje = "El número de días debe ser un número entero."
        if mensaje != "":
            print(mensaje)
            seguir = False

        if seguir:
            try:
                minimo = int(input("Habitaciones ocupadas mínimas: "))
                mensaje = hotel.validar_ocupadas(minimo)
            except ValueError:
                mensaje = "Las habitaciones ocupadas deben ser un número entero."
            if mensaje != "":
                print(mensaje)
                seguir = False

        if seguir:
            try:
                maximo = int(input("Habitaciones ocupadas máximas: "))
                mensaje = hotel.validar_ocupadas(maximo)
            except ValueError:
                mensaje = "Las habitaciones ocupadas deben ser un número entero."
            if mensaje != "":
                print(mensaje)
                seguir = False

        if seguir:
            mensaje = hotel.simular_dias(dias, minimo, maximo)
            if mensaje == "":
                print(f"Se simularon {dias} día(s).")
                print(f"Habitaciones ocupadas simuladas: {hotel.ocupadas[-dias:]}")
            else:
                print(mensaje)


def opcion_ver_informe(cadena: CadenaHotelera) -> None:
    hotel = pedir_hotel(cadena)
    if hotel is not None:
        print()
        print(f"Hotel: {hotel.nombre}")
        print(f"Habitaciones habilitadas: {hotel.habitaciones}")
        if hotel.dias_registrados() == 0:
            print("El hotel no tiene días registrados.")
        else:
            print(f"Días registrados: {hotel.dias_registrados()}")
            print(f"Noches vendidas: {hotel.noches_vendidas()}")
            print(f"Promedio de habitaciones ocupadas por día: {round(hotel.promedio(), 2)}")
            print(f"Porcentaje de ocupación: {round(hotel.porcentaje_ocupacion(), 2)} %")
            print(f"Desviación estándar: {round(hotel.desviacion_estandar(), 2)}")
            print(f"Día con más habitaciones ocupadas: {hotel.dia_mas_ocupado()}")
            print(f"Día con menos habitaciones ocupadas: {hotel.dia_menos_ocupado()}")


def opcion_salir(cadena: CadenaHotelera) -> None:
    print("Fin del programa.")


def main() -> None:
    cadena = CadenaHotelera()
    salir = False
    while not salir:
        limpiar_consola()
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            opcion_crear_hotel(cadena)
        elif opcion == "2":
            opcion_registrar_dia(cadena)
        elif opcion == "3":
            opcion_simular_dias(cadena)
        elif opcion == "4":
            opcion_ver_informe(cadena)
        elif opcion == "7":
            opcion_salir(cadena)
            salir = True
        else:
            print("La opción no es válida.")
        if not salir:
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
