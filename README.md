# Software_FJ_Fase4

## Sistema de gestión de clientes, servicios y reservas

Este proyecto se realiza como parte de la actividad Fase 4 del curso de Programación de la UNAD. Consiste en crear un sistema para la empresa Software FJ, donde se puedan registrar clientes, crear servicios y manejar sus reservas.

Para desarrollar este programa utilizamos Python y programación orientada a objetos. También trabajamos sin utilizar bases de datos.

## ¿Qué puede hacer el sistema?

El programa permite realizar las siguientes actividades:

- Registrar clientes y revisar que sus datos estén correctos.
- Crear servicios para reservar salas, alquilar equipos y solicitar asesorías.
- Calcular el costo de los servicios con impuestos y descuentos.
- Crear, confirmar, cancelar y procesar reservas.
- Controlar los errores que puedan aparecer durante el funcionamiento del programa.
- Guardar registros de las actividades y los errores que ocurren.
- Realizar pruebas para comprobar que el sistema funcione correctamente.

## Archivos del proyecto

El proyecto está organizado en varios archivos y cada uno cumple una función:

- `main.py`: es el archivo principal desde donde ejecutamos el sistema.
- `modelos.py`: contiene las clases que utilizamos para manejar los clientes.
- `servicios.py`: contiene las clases para crear las reservas de salas, los alquileres de equipos y las asesorías.
- `reservas.py`: permite crear, confirmar, cancelar y procesar las reservas.
- `excepciones.py`: contiene los errores que creamos para controlar diferentes situaciones.
- `logs.py`: guarda los registros de las actividades y los errores del programa.
- `prueba_servicios.py`: contiene las pruebas que realizamos para comprobar el funcionamiento de los servicios.
- `.gitignore`: evita que se suban algunos archivos temporales al repositorio.

## Requisitos para ejecutar el programa

Para utilizar el sistema necesitamos:

- Tener Python instalado.
- Contar con un editor de código, como Visual Studio Code.

## ¿Cómo ejecutar el programa?

Para ejecutar el sistema debemos seguir estos pasos:

1. Descargar o clonar el repositorio de GitHub.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir la terminal.
4. Escribir el siguiente comando para ejecutar el programa principal:

   `py main.py`

5. Para realizar las pruebas de los servicios, escribimos:

   `py prueba_servicios.py`

## Trabajo en equipo

Este proyecto se está desarrollando en equipo. Para compartir los archivos y los cambios que vamos realizando, utilizamos Git y GitHub. Así cada integrante puede aportar al desarrollo del sistema y mantener actualizado el trabajo.

## Repositorio de GitHub

En el siguiente enlace se puede encontrar el proyecto y revisar los archivos que hemos desarrollado:

https://github.com/Yaandradea/Software_FJ_Fase4
