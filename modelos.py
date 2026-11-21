
from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError


# Esta es la clase principal que nos sirve como base para otras clases.
class Entidad(ABC):

    def __init__(self, identificacion):
        # Revisamos que la identificación no esté vacía.
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ValueError("La identificación es obligatoria.")

        # Guardamos la identificación para que no se pueda cambiar directamente.
        self.__identificacion = identificacion.strip()

    # Con esta propiedad podemos consultar la identificación.
    @property
    def identificacion(self):
        return self.__identificacion

    # Cada clase que herede de Entidad debe tener este método.
    @abstractmethod
    def mostrar_informacion(self):
        pass


# Esta clase guarda la información de cada cliente.
class Cliente(Entidad):

    def __init__(self, nombre, identificacion, correo, telefono):

        # Revisamos que el nombre no esté vacío.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ClienteInvalidoError("El nombre del cliente es obligatorio.")

        # Revisamos que el correo tenga un formato básico válido.
        if (
            not isinstance(correo, str)
            or "@" not in correo
            or "." not in correo.split("@")[-1]
        ):
            raise ClienteInvalidoError("El correo electrónico no es válido.")

        # Revisamos que el teléfono tenga entre 7 y 15 números.
        if (
            not isinstance(telefono, str)
            or not telefono.isdigit()
            or not 7 <= len(telefono) <= 15
        ):
            raise ClienteInvalidoError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        # Llamamos al constructor de la clase principal.
        super().__init__(identificacion)

        # Guardamos los datos del cliente.
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

    # Estas propiedades nos permiten consultar los datos del cliente.
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    # Con esta propiedad podemos cambiar el correo, pero primero lo revisamos.
    @correo.setter
    def correo(self, nuevo_correo):
        if (
            not isinstance(nuevo_correo, str)
            or "@" not in nuevo_correo
            or "." not in nuevo_correo.split("@")[-1]
        ):
            raise ClienteInvalidoError("El nuevo correo no es válido.")

        self.__correo = nuevo_correo.strip()

    @property
    def telefono(self):
        return self.__telefono

    # Este método muestra los datos del cliente.
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Identificación: {self.identificacion}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
