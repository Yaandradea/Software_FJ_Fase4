
from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError


# Esta es la clase principal que sirve como base para otras clases.
class Entidad(ABC):

    def __init__(self, identificacion):

        # Revisamos que la identificación sea un texto válido.
        if (
            not isinstance(identificacion, str)
            or not identificacion.strip()
        ):
            raise ValueError("La identificación es obligatoria.")

        # Guardamos la identificación como un dato privado.
        self.__identificacion = identificacion.strip()

    # Esta propiedad permite consultar la identificación.
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

        # Revisamos que el nombre sea válido.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre del cliente es obligatorio."
            )

        # Revisamos que el correo tenga un formato básico válido.
        if (
            not isinstance(correo, str)
            or correo.count("@") != 1
            or " " in correo.strip()
            or "." not in correo.split("@")[-1]
            or correo.startswith("@")
            or correo.endswith("@")
            or correo.split("@")[-1].startswith(".")
            or correo.split("@")[-1].endswith(".")
        ):
            raise ClienteInvalidoError(
                "El correo electrónico no es válido."
            )

        # Revisamos que el teléfono tenga entre 7 y 15 dígitos.
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

        # Guardamos los datos del cliente como atributos privados.
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

    # Esta propiedad permite consultar el nombre.
    @property
    def nombre(self):
        return self.__nombre

    # Esta propiedad permite consultar y modificar el correo.
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):

        # Revisamos que el nuevo correo tenga un formato válido.
        if (
            not isinstance(nuevo_correo, str)
            or nuevo_correo.count("@") != 1
            or " " in nuevo_correo.strip()
            or "." not in nuevo_correo.split("@")[-1]
            or nuevo_correo.startswith("@")
            or nuevo_correo.endswith("@")
            or nuevo_correo.split("@")[-1].startswith(".")
            or nuevo_correo.split("@")[-1].endswith(".")
        ):
            raise ClienteInvalidoError(
                "El nuevo correo no es válido."
            )

        self.__correo = nuevo_correo.strip()

    # Esta propiedad permite consultar el teléfono.
    @property
    def telefono(self):
        return self.__telefono

    # Este método muestra la información del cliente.
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Identificación: {self.identificacion}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
