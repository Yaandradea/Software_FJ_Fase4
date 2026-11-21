
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from logs import registrar_evento, registrar_error


print("SISTEMA DE PRUEBA DE SERVICIOS - SOFTWARE FJ")

servicios = []

try:
    sala = ReservaSala("Sala de reuniones", 50000)
    servicios.append(sala)
    print("\nServicio creado:", sala.describir_servicio())
    registrar_evento("Se creó una reserva de sala.")

except Exception as error:
    print("Error al crear la sala:", error)
    registrar_error(f"Error al crear sala: {error}")


try:
    equipo = AlquilerEquipo("Computador portátil", 30000)
    servicios.append(equipo)
    print("\nServicio creado:", equipo.describir_servicio())
    registrar_evento("Se creó un alquiler de equipo.")

except Exception as error:
    print("Error al crear el equipo:", error)
    registrar_error(f"Error al crear equipo: {error}")


try:
    asesoria = Asesoria("Asesoría tecnológica", 100000)
    servicios.append(asesoria)
    print("\nServicio creado:", asesoria.describir_servicio())
    registrar_evento("Se creó una asesoría.")

except Exception as error:
    print("Error al crear la asesoría:", error)
    registrar_error(f"Error al crear asesoría: {error}")


try:
    costo = sala.calcular_costo(2)
    print("\nCosto de la sala:", costo)
    registrar_evento("Se calculó el costo de la sala.")

except Exception as error:
    print("Error:", error)
    registrar_error(str(error))


try:
    costo = equipo.calcular_costo(2)
    print("\nCosto del equipo:", costo)
    registrar_evento("Se calculó el costo del equipo.")

except Exception as error:
    print("Error:", error)
    registrar_error(str(error))


try:
    costo = asesoria.calcular_costo(2, impuesto=19)
    print("\nCosto de asesoría con impuesto:", costo)
    registrar_evento("Se calculó la asesoría con impuesto.")

except Exception as error:
    print("Error:", error)
    registrar_error(str(error))


try:
    costo = sala.calcular_costo(2, descuento=10)
    print("\nCosto de sala con descuento:", costo)
    registrar_evento("Se calculó la sala con descuento.")

except Exception as error:
    print("Error:", error)
    registrar_error(str(error))


try:
    servicio_invalido = ReservaSala("Sala incorrecta", -5000)

except Exception as error:
    print("\nError controlado:", error)
    registrar_error(f"Intento de crear servicio inválido: {error}")


try:
    costo = equipo.calcular_costo(0)

except Exception as error:
    print("\nError controlado:", error)
    registrar_error(f"Duración incorrecta: {error}")


try:
    sala.disponible = False
    costo = sala.calcular_costo(2)

except Exception as error:
    print("\nError controlado:", error)
    registrar_error(f"Servicio no disponible: {error}")


print("\nLas pruebas finalizaron.")
print("El programa continuó ejecutándose a pesar de los errores.")
