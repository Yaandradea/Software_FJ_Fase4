
from modelos import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva

from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    DatoFaltanteError
)

from logs import (
    registrar_evento,
    registrar_advertencia,
    registrar_error
)


# Estas listas guardan la información mientras se ejecuta el programa.
clientes = []
servicios = []
reservas = []


# Inicializamos las variables para evitar errores si algo falla.
cliente1 = None
sala = None
equipo = None
asesoria = None
reserva1 = None


# Esta función muestra el título del sistema.
def mostrar_titulo():
    print("=" * 55)
    print("       SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ")
    print("=" * 55)


# Aquí comienza el programa principal.
def main():

    global cliente1, sala, equipo, asesoria, reserva1

    mostrar_titulo()

    print("\n1. REGISTRO DE CLIENTES")

    # Creamos un cliente con todos sus datos correctos.
    try:
        cliente1 = Cliente(
            "Carlos Pérez",
            "1001",
            "carlos@gmail.com",
            "3101234567"
        )

        clientes.append(cliente1)

        print("Cliente registrado correctamente.")
        print(cliente1.mostrar_informacion())

        registrar_evento("Se registró un cliente correctamente.")

    except (ClienteInvalidoError, ValueError) as error:
        print("No se pudo registrar el cliente:", error)
        registrar_error(str(error))

    # Intentamos registrar un cliente con información incorrecta.
    try:
        cliente2 = Cliente(
            "",
            "1002",
            "correo incorrecto",
            "123"
        )

        clientes.append(cliente2)

    except (ClienteInvalidoError, ValueError) as error:
        print("\nError al registrar el segundo cliente:", error)
        registrar_advertencia(
            "Se intentó registrar un cliente con datos incorrectos."
        )

    print("\n2. CREACIÓN DE SERVICIOS")

    # Creamos los tres tipos de servicios de la empresa.
    try:
        sala = ReservaSala("Sala de reuniones", 50000)
        equipo = AlquilerEquipo("Computador portátil", 30000)
        asesoria = Asesoria("Asesoría de software", 80000)

        servicios.extend([sala, equipo, asesoria])

        print("Los tres servicios se crearon correctamente.")

        registrar_evento("Se crearon los servicios del sistema.")

    except ValueError as error:
        print("Error al crear los servicios:", error)
        registrar_error(str(error))

    # Intentamos crear un servicio con una tarifa incorrecta.
    try:
        servicio_invalido = ReservaSala("Sala pequeña", -10000)
        servicios.append(servicio_invalido)

    except ValueError as error:
        print("\nNo se pudo crear el servicio:", error)
        registrar_advertencia(
            "Se intentó crear un servicio con una tarifa incorrecta."
        )

    print("\n3. PRUEBAS DE COSTOS")

    # Calculamos el costo de cada servicio.
    for servicio in servicios:

        try:
            costo = servicio.calcular_costo(2)

            print(
                servicio.describir_servicio(),
                "- Costo por 2 horas:",
                f"${costo:,.2f}"
            )

        except (ServicioNoDisponibleError, ValueError) as error:
            print("No se pudo calcular el servicio:", error)
            registrar_error(str(error))

    # Probamos un costo con impuestos y descuentos.
    if sala is not None:
        try:
            total = sala.calcular_costo(
                2,
                impuesto=19,
                descuento=10
            )

            print("\nCosto de la sala con impuestos y descuento:")
            print(f"${total:,.2f}")

            registrar_evento(
                "Se calculó un servicio con impuestos y descuentos."
            )

        except (ServicioNoDisponibleError, ValueError) as error:
            print("Error al calcular el costo:", error)
            registrar_error(str(error))

    # Intentamos utilizar un servicio que no está disponible.
    if equipo is not None:
        try:
            equipo.disponible = False
            equipo.calcular_costo(2)

        except ServicioNoDisponibleError as error:
            print("\nNo se puede utilizar el equipo:", error)
            registrar_advertencia(
                "Se intentó utilizar un servicio no disponible."
            )

        finally:
            # Dejamos el equipo disponible para las siguientes pruebas.
            equipo.disponible = True
            print("Terminó la prueba de disponibilidad.")

    print("\n4. GESTIÓN DE RESERVAS")

    # Creamos una reserva válida para el primer cliente.
    if cliente1 is not None and sala is not None:
        try:
            reserva1 = Reserva(cliente1, sala, 2)

            reservas.append(reserva1)

            print("\nReserva creada correctamente.")
            print(reserva1.mostrar_reserva())

            registrar_evento("Se creó una reserva correctamente.")

        except (ReservaInvalidaError, ValueError) as error:
            print("No se pudo crear la reserva:", error)
            registrar_error(str(error))

    # Intentamos crear una reserva con una duración incorrecta.
    if cliente1 is not None and sala is not None:
        try:
            reserva_invalida = Reserva(cliente1, sala, -2)
            reservas.append(reserva_invalida)

        except (ReservaInvalidaError, ValueError) as error:
            print("\nNo se pudo crear la reserva:", error)
            registrar_advertencia(
                "Se intentó crear una reserva con duración incorrecta."
            )

    # Intentamos crear una reserva sin enviar los datos necesarios.
    try:
        reserva_sin_datos = Reserva()

    except DatoFaltanteError as error:
        print("\nNo se pudo crear la reserva:", error)
        registrar_advertencia(
            "Se intentó crear una reserva sin datos obligatorios."
        )

    # Confirmamos la primera reserva.
    if reserva1 is not None:
        try:
            mensaje = reserva1.confirmar()

        except (OperacionNoPermitidaError, ServicioNoDisponibleError) as error:
            print("No se pudo confirmar la reserva:", error)
            registrar_error(str(error))

        else:
            print("\n", mensaje)
            registrar_evento("La reserva fue confirmada.")

        finally:
            print("Terminó el intento de confirmación.")

    # Procesamos la reserva después de confirmarla.
    if reserva1 is not None:
        try:
            total_reserva = reserva1.procesar()

            print("\nReserva procesada correctamente.")
            print(f"Total de la reserva: ${total_reserva:,.2f}")

            registrar_evento(
                "La reserva fue procesada correctamente."
            )

        except (OperacionNoPermitidaError, ReservaInvalidaError) as error:
            print("No se pudo procesar la reserva:", error)
            registrar_error(str(error))

    # Creamos otra reserva para probar la cancelación.
    if cliente1 is not None and asesoria is not None:
        try:
            reserva2 = Reserva(cliente1, asesoria, 1)

            reservas.append(reserva2)

            print("\nSegunda reserva creada correctamente.")

            mensaje = reserva2.cancelar()

            print(mensaje)

            registrar_evento(
                "Se creó y canceló una segunda reserva."
            )

        except (
            ReservaInvalidaError,
            OperacionNoPermitidaError,
            ValueError
        ) as error:
            print("No se pudo completar la operación:", error)
            registrar_error(str(error))

    print("\n5. RESUMEN DEL SISTEMA")

    # Mostramos cuántos elementos quedaron guardados.
    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas realizadas:", len(reservas))

    print("\nInformación de las reservas:")

    for reserva in reservas:
        print("-" * 40)
        print(reserva.mostrar_reserva())

    print("\nEl sistema terminó sus pruebas.")

    registrar_evento("Finalizó la ejecución del sistema.")


# Esta condición permite ejecutar el programa desde este archivo.
if __name__ == "__main__":
    main()
