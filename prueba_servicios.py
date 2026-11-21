
from servicios import (
    Servicio,
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)

from excepciones import ServicioNoDisponibleError
from logs import (
    registrar_evento,
    registrar_advertencia,
    registrar_error
)


print("SISTEMA DE PRUEBA DE SERVICIOS - SOFTWARE FJ")

servicios = []

# Inicializamos las variables para evitar errores si falla una creación.
sala = None
equipo = None
asesoria = None


print("\n1. CREACIÓN DE SERVICIOS")

# Creamos una reserva de sala.
try:
    sala = ReservaSala("Sala de reuniones", 50000)
    servicios.append(sala)

    print("\nServicio creado:", sala.describir_servicio())

    registrar_evento("Se creó una reserva de sala.")

except ValueError as error:
    print("Error al crear la sala:", error)
    registrar_error(f"Error al crear sala: {error}")


# Creamos un alquiler de equipo.
try:
    equipo = AlquilerEquipo("Computador portátil", 30000)
    servicios.append(equipo)

    print("\nServicio creado:", equipo.describir_servicio())

    registrar_evento("Se creó un alquiler de equipo.")

except ValueError as error:
    print("Error al crear el equipo:", error)
    registrar_error(f"Error al crear equipo: {error}")


# Creamos una asesoría.
try:
    asesoria = Asesoria("Asesoría tecnológica", 100000)
    servicios.append(asesoria)

    print("\nServicio creado:", asesoria.describir_servicio())

    registrar_evento("Se creó una asesoría.")

except ValueError as error:
    print("Error al crear la asesoría:", error)
    registrar_error(f"Error al crear asesoría: {error}")


print("\n2. PRUEBA DE POLIMORFISMO")

# Recorremos los servicios usando la misma lista.
# Cada objeto utiliza sus propios métodos.
for servicio in servicios:

    try:
        print("\nDescripción:", servicio.describir_servicio())

        costo = servicio.calcular_costo(2)

        print("Costo por 2 horas:", f"${costo:,.2f}")

        registrar_evento(
            f"Se calculó el costo de: {servicio.describir_servicio()}."
        )

    except (ServicioNoDisponibleError, ValueError) as error:
        print("No se pudo calcular el servicio:", error)
        registrar_error(str(error))


print("\n3. PRUEBAS DE IMPUESTOS Y DESCUENTOS")

# Calculamos el costo de la asesoría con impuestos.
if asesoria is not None:
    try:
        costo = asesoria.calcular_costo(2, impuesto=19)

        print("\nCosto de asesoría con impuesto:")
        print(f"${costo:,.2f}")

        registrar_evento("Se calculó la asesoría con impuesto.")

    except (ServicioNoDisponibleError, ValueError) as error:
        print("Error:", error)
        registrar_error(str(error))


# Calculamos el costo de la sala con descuento.
if sala is not None:
    try:
        costo = sala.calcular_costo(2, descuento=10)

        print("\nCosto de sala con descuento:")
        print(f"${costo:,.2f}")

        registrar_evento("Se calculó la sala con descuento.")

    except (ServicioNoDisponibleError, ValueError) as error:
        print("Error:", error)
        registrar_error(str(error))


print("\n4. PRUEBAS DE ERRORES")

# Intentamos crear un servicio con una tarifa incorrecta.
try:
    servicio_invalido = ReservaSala("Sala incorrecta", -5000)

except ValueError as error:
    print("\nError controlado:", error)

    registrar_advertencia(
        f"Intento de crear servicio inválido: {error}"
    )


# Intentamos calcular un servicio con duración incorrecta.
if equipo is not None:
    try:
        costo = equipo.calcular_costo(0)

    except ValueError as error:
        print("\nError controlado:", error)

        registrar_advertencia(
            f"Duración incorrecta: {error}"
        )


# Intentamos utilizar un servicio que no está disponible.
if sala is not None:
    try:
        sala.disponible = False
        sala.calcular_costo(2)

    except ServicioNoDisponibleError as error:
        print("\nError controlado:", error)

        registrar_advertencia(
            f"Servicio no disponible: {error}"
        )

    finally:
        # Dejamos nuevamente disponible la sala.
        sala.disponible = True

        print("Terminó la prueba de disponibilidad.")


print("\nLas pruebas finalizaron.")
print("El programa continuó ejecutándose a pesar de los errores.")

registrar_evento("Finalizaron las pruebas independientes de servicios.")
