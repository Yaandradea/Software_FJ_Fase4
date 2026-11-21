
from modelos import Cliente
from servicios import Servicio
from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    DatoFaltanteError
)
from logs import registrar_evento


# Esta clase nos permite crear y manejar las reservas de los clientes.
class Reserva:

    def __init__(self, cliente, servicio, duracion):

        # Revisamos que los datos necesarios para la reserva estén completos.
        if cliente is None or servicio is None or duracion is None:
            raise DatoFaltanteError(
                "Faltan datos para poder crear la reserva."
            )

        # Comprobamos que el cliente sea un objeto de la clase Cliente.
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "El cliente ingresado no es válido."
            )

        # Comprobamos que el servicio pertenezca a la clase Servicio.
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "El servicio ingresado no es válido."
            )

        # Revisamos que la duración sea un número mayor que cero.
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ReservaInvalidaError(
                "La duración debe ser un número mayor que cero."
            )

        # Guardamos la información de la reserva.
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        # Avisamos que se creó una nueva reserva.
        registrar_evento(
            f"Se creó una reserva para el cliente {cliente.nombre}."
        )

    # Estas propiedades permiten consultar la información de la reserva.
    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    # Este método permite calcular el costo de la reserva.
    # También podemos agregar impuestos y descuentos si se necesitan.
    def calcular_total(self, impuesto=0, descuento=0):
        try:
            total = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )
            return total

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

    # Este método permite confirmar una reserva.
    def confirmar(self):

        # Solo se pueden confirmar las reservas que están pendientes.
        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Esta reserva no se puede confirmar."
            )

        # Revisamos que el servicio todavía esté disponible.
        self.__servicio.validar_disponibilidad()

        self.__estado = "Confirmada"

        registrar_evento(
            f"Se confirmó la reserva del cliente {self.__cliente.nombre}."
        )

        return "La reserva fue confirmada correctamente."

    # Este método permite cancelar una reserva.
    def cancelar(self):

        # No permitimos cancelar una reserva que ya fue procesada.
        if self.__estado == "Procesada":
            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva que ya fue procesada."
            )

        # Tampoco permitimos cancelar una reserva que ya estaba cancelada.
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "Esta reserva ya se encuentra cancelada."
            )

        self.__estado = "Cancelada"

        registrar_evento(
            f"Se canceló la reserva del cliente {self.__cliente.nombre}."
        )

        return "La reserva fue cancelada correctamente."

    # Este método permite procesar una reserva que ya fue confirmada.
    def procesar(self):

        # Primero comprobamos que la reserva esté confirmada.
        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "Solo se pueden procesar las reservas confirmadas."
            )

        # Calculamos el valor de la reserva.
        total = self.calcular_total()

        self.__estado = "Procesada"

        registrar_evento(
            f"Se procesó la reserva del cliente {self.__cliente.nombre}."
        )

        return total

    # Este método muestra toda la información de la reserva.
    def mostrar_reserva(self):
        return (
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.describir_servicio()}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}"
        )
