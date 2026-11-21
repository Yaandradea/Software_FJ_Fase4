
# Aquí creamos un error para cuando los datos del cliente estén mal.
class ClienteInvalidoError(Exception):
    pass


# Este error aparece cuando queremos usar un servicio que no está disponible.
class ServicioNoDisponibleError(Exception):
    pass


# Aquí avisamos cuando los datos de una reserva no son correctos.
class ReservaInvalidaError(Exception):
    pass


# Este error aparece cuando intentamos hacer algo que no está permitido.
class OperacionNoPermitidaError(Exception):
    pass


# Aquí mostramos un error cuando hace falta un dato obligatorio.
class DatoFaltanteError(Exception):
    pass
