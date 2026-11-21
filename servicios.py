from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


class Servicio(ABC):

    def __init__(self, nombre, tarifa):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if not isinstance(tarifa, (int, float)) or isinstance(tarifa, bool) or tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.tarifa = tarifa
        self.disponible = True

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no está disponible."
            )

    def validar_duracion(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duración debe ser un número mayor que cero.")

    def aplicar_impuestos_descuentos(
        self, costo, impuesto=0, descuento=0
    ):
        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        total = costo + (costo * impuesto / 100)
        total = total - (total * descuento / 100)

        return total

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_duracion(duracion)

        costo = self.tarifa * duracion

        return self.aplicar_impuestos_descuentos(
            costo, impuesto, descuento
        )

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_duracion(duracion)

        costo = self.tarifa * duracion

        return self.aplicar_impuestos_descuentos(
            costo, impuesto, descuento
        )

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"


class Asesoria(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_duracion(duracion)

        costo = self.tarifa * duracion

        return self.aplicar_impuestos_descuentos(
            costo, impuesto, descuento
        )

    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}"
