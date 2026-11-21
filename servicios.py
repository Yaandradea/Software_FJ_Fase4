
from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


# Esta clase sirve como base para los diferentes servicios.
class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        # Revisamos que el nombre del servicio no esté vacío.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        # Comprobamos que la tarifa sea un número mayor que cero.
        if (
            not isinstance(tarifa, (int, float))
            or isinstance(tarifa, bool)
            or tarifa <= 0
        ):
            raise ValueError("La tarifa debe ser mayor que cero.")

        # Guardamos los datos como atributos privados.
        self.__nombre = nombre.strip()
        self.__tarifa = tarifa
        self.__disponible = True

    # Estas propiedades permiten consultar los datos del servicio.
    @property
    def nombre(self):
        return self.__nombre

    @property
    def tarifa(self):
        return self.__tarifa

    @property
    def disponible(self):
        return self.__disponible

    # Esta propiedad permite cambiar la disponibilidad.
    @disponible.setter
    def disponible(self, nuevo_estado):

        if not isinstance(nuevo_estado, bool):
            raise ValueError(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self.__disponible = nuevo_estado

    # Revisamos si el servicio está disponible.
    def validar_disponibilidad(self):

        if not self.__disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.__nombre} no está disponible."
            )

    # Comprobamos que la duración sea correcta.
    def validar_duracion(self, duracion):

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError(
                "La duración debe ser un número mayor que cero."
            )

    # Revisamos que los impuestos y descuentos sean válidos.
    def validar_porcentajes(self, impuesto, descuento):

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 100
        ):
            raise ValueError(
                "El impuesto debe estar entre 0 y 100."
            )

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 100
        ):
            raise ValueError(
                "El descuento debe estar entre 0 y 100."
            )

    # Este método revisa los parámetros generales del servicio.
    def validar_parametros(self, duracion, impuesto=0, descuento=0):

        self.validar_duracion(duracion)
        self.validar_porcentajes(impuesto, descuento)

    # Calculamos el costo aplicando impuestos y descuentos.
    def aplicar_impuestos_descuentos(
        self, costo, impuesto=0, descuento=0
    ):

        # Comprobamos que los porcentajes sean correctos.
        self.validar_porcentajes(impuesto, descuento)

        total = costo + (costo * impuesto / 100)
        total = total - (total * descuento / 100)

        return total

    # Cada servicio debe tener su propia forma de calcular el costo.
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    # Cada servicio debe tener una descripción.
    @abstractmethod
    def describir_servicio(self):
        pass


# Esta clase representa las reservas de salas.
class ReservaSala(Servicio):

    # Sobrescribimos la validación de parámetros.
    def validar_parametros(self, duracion, impuesto=0, descuento=0):

        # Utilizamos las validaciones generales de la clase principal.
        super().validar_parametros(duracion, impuesto, descuento)

    # Calculamos el costo de la reserva de sala.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_disponibilidad()
        self.validar_parametros(duracion, impuesto, descuento)

        costo = self.tarifa * duracion

        return self.aplicar_impuestos_descuentos(
            costo, impuesto, descuento
        )

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"


# Esta clase representa el alquiler de equipos.
class AlquilerEquipo(Servicio):

    # Sobrescribimos la validación de parámetros.
    def validar_parametros(self, duracion, impuesto=0, descuento=0):

        # Utilizamos las validaciones generales de la clase principal.
        super().validar_parametros(duracion, impuesto, descuento)

    # Calculamos el costo del alquiler de equipo.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_disponibilidad()
        self.validar_parametros(duracion, impuesto, descuento)

        costo = self.tarifa * duracion

        return self.aplicar_impuestos_descuentos(
            costo, impuesto, descuento
        )

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"


# Esta clase representa las asesorías especializadas.
class Asesoria(Servicio):

    # Sobrescribimos la validación de parámetros.
    def validar_parametros(self, duracion, impuesto=0, descuento=0):

        # Utilizamos las validaciones generales de la clase principal.
        super().validar_parametros(duracion, impuesto, descuento)

    # Calculamos el costo de la asesoría.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_disponibilidad()
        self.validar_parametros(duracion, impuesto, descuento)

        costo = self.tarifa * duracion

        return self.aplicar_impuestos_descuentos(
            costo, impuesto, descuento
        )

    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}"
