import math
import random
from datetime import date, timedelta


def es_entero(texto: str) -> bool:
    resultado = True
    try:
        int(texto)
    except ValueError:
        resultado = False
    return resultado


def crear_fecha(anio: str, mes: str, dia: str) -> date | None:
    fecha = None
    try:
        fecha = date(int(anio), int(mes), int(dia))
    except ValueError:
        fecha = None
    return fecha


def validar_dias_a_simular(dias: int) -> str:
    mensaje = ""
    if dias < 1:
        mensaje = "Se debe simular al menos un día."
    elif dias > 365:
        # Decisión: máximo 365 días por simulación para que el programa no se quede pegado.
        mensaje = "Se pueden simular máximo 365 días cada vez."
    return mensaje


class Hotel:
    def __init__(self, nombre: str, habitaciones: int, fecha_inicio: date) -> None:
        self.nombre = nombre
        self.habitaciones = habitaciones
        self.fecha_inicio = fecha_inicio
        self.ocupadas: list[int] = []

    def dias_registrados(self) -> int:
        return len(self.ocupadas)

    def fecha_del_dia(self, posicion: int) -> date:
        return self.fecha_inicio + timedelta(days=posicion)

    def fecha_siguiente(self) -> date:
        return self.fecha_del_dia(len(self.ocupadas))

    def ultimo_dia(self) -> date | None:
        ultimo = None
        # Decisión: si la lista está vacía no hay último día.
        if len(self.ocupadas) > 0:
            ultimo = self.fecha_del_dia(len(self.ocupadas) - 1)
        return ultimo

    def validar_ocupadas(self, cantidad: int) -> str:
        mensaje = ""
        if cantidad < 0 or cantidad > self.habitaciones:
            mensaje = f"Las habitaciones ocupadas de {self.nombre} van de 0 a {self.habitaciones}."
        return mensaje

    def registrar_dia(self, cantidad: int) -> None:
        self.ocupadas.append(cantidad)

    def simular_dias(self, dias: int, minimo: int, maximo: int) -> str:
        mensaje = ""
        if minimo > maximo:
            mensaje = "El mínimo no puede ser mayor que el máximo."
        else:
            for i in range(dias):
                self.ocupadas.append(random.randint(minimo, maximo))
        return mensaje

    def noches_vendidas(self) -> int:
        total = 0
        for cantidad in self.ocupadas:
            total = total + cantidad
        return total

    def promedio(self) -> float:
        resultado = 0.0
        # Decisión: sin días registrados se devuelve 0 para no dividir entre cero.
        if len(self.ocupadas) > 0:
            resultado = self.noches_vendidas() / len(self.ocupadas)
        return resultado

    def porcentaje_ocupacion(self) -> float:
        resultado = 0.0
        if len(self.ocupadas) > 0:
            resultado = self.promedio() / self.habitaciones * 100
        return resultado

    def desviacion_estandar(self) -> float:
        resultado = 0.0
        if len(self.ocupadas) > 0:
            promedio = self.promedio()
            suma = 0.0
            for cantidad in self.ocupadas:
                suma = suma + (cantidad - promedio) ** 2
            resultado = math.sqrt(suma / len(self.ocupadas))
        return resultado

    def dia_mas_ocupado(self) -> date | None:
        dia = None
        if len(self.ocupadas) > 0:
            posicion_mayor = 0
            for i in range(len(self.ocupadas)):
                # Decisión: con > (y no >=) en un empate se queda el primer día.
                if self.ocupadas[i] > self.ocupadas[posicion_mayor]:
                    posicion_mayor = i
            dia = self.fecha_del_dia(posicion_mayor)
        return dia

    def dia_menos_ocupado(self) -> date | None:
        dia = None
        if len(self.ocupadas) > 0:
            posicion_menor = 0
            for i in range(len(self.ocupadas)):
                if self.ocupadas[i] < self.ocupadas[posicion_menor]:
                    posicion_menor = i
            dia = self.fecha_del_dia(posicion_menor)
        return dia


class CadenaHotelera:
    def __init__(self) -> None:
        self.hoteles: list[Hotel] = []

    def buscar_hotel(self, nombre: str) -> Hotel | None:
        nombre = nombre.strip()
        encontrado = None
        i = 0
        while i < len(self.hoteles) and encontrado is None:
            if self.hoteles[i].nombre == nombre:
                encontrado = self.hoteles[i]
            i = i + 1
        return encontrado

    def crear_hotel(self, nombre: str, habitaciones: str, anio: str, mes: str, dia: str) -> str:
        nombre = nombre.strip()
        fecha = crear_fecha(anio, mes, dia)
        mensaje = ""
        if nombre == "":
            mensaje = "El nombre no puede estar vacío."
        elif self.buscar_hotel(nombre) is not None:
            mensaje = f"Ya existe un hotel llamado {nombre}."
        elif not es_entero(habitaciones):
            mensaje = "Las habitaciones habilitadas deben ser un número entero."
        elif int(habitaciones) < 1:
            mensaje = "El hotel debe tener al menos una habitación habilitada."
        elif fecha is None:
            mensaje = "La fecha no es válida."
        else:
            self.hoteles.append(Hotel(nombre, int(habitaciones), fecha))
        return mensaje
