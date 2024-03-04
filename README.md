# ST0263 Tópicos Especiales en Telemática

* Estudiante: David Gonzalez Tamayo, dgonzalez2@eafit.edu.co

* Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Nombre de la actividad

## 1. Breve descripción de la actividad
Desarrollar un sistema P2P distribuido y descentralizado con el objetivo de compartir archivos. Esta implementación se debe basar en un esquema de red no estructurado en el cual un servidor central sirva como directorio y localizador. Un peer está compuesto por un cliente y un servidor. El cliente se debe comunicar con el servidor central para cargar y descargar archivos, este le debe responder con la dirección de un peer que contenga el archivo a descargar o que tenga espacio para cargar un archivo. El servidor del peer debe comunicarse con el servidor central para darle su estado y los archivos que contiene.

## 1.1. Qué aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

* Se desarrolló un sistema P2P distribuido y descentralizado.
Implementación basada en un esquema de red no estructurado con un servidor central como directorio y localizador.
* Comunicación entre cliente y servidor central para cargar y descargar archivos.
Respuesta del servidor central con la dirección de un peer para las operaciones de carga o descarga.
* Comunicación del servidor del peer con el servidor central para informar su estado y los archivos contenidos.

## 1.2. Qué aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se requiere más especificación sobre los aspectos que no se han cumplido o desarrollado.

## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Se utilizaron las siguientes tecnologías y prácticas:

* Arquitectura cliente-servidor.
* Implementación de servidor central utilizando FastAPI en Python.
* Implementación de servidor de descargas utilizando gRPC.
* Interfaz gráfica de cliente desarrollada con Jinja y FastAPI.
* Implementación de un proxy en .NET utilizando YARP para redirigir las peticiones a los diferentes servidores.

![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/d886c07c-1ef9-40ed-bfc9-f8e4c79f0a9f)

## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
* Lenguaje de programación: Python, .NET
* Librerías y paquetes utilizados:
    * FastAPI
    * gRPC
    * Jinja
    * YARP

## Detalles de desarrollo

### Configuración de parámetros del proyecto

* Dirección IP: Se configura mediante el parámetro CENTRAL_HOST en el archivo docker-compose.yml.
* Puertos: Los puertos están definidos en el archivo docker-compose.yml para cada servicio.

## Estructura del proyecto

```
Project_Root/
│
├── PServer/
│   ├── app.py
│   ├── Dockerfile
│   └── ...
│
├── PClient/
│   ├── app.py
│   ├── Dockerfile
│   └── ...
│
├── CentralServer/
│   ├── app.py
│   ├── Dockerfile
│   └── ...
│
├── ErgoProxy/
│   ├── Program.cs
│   ├── Dockerfile
│   └── ...
│
├── files/
│   ├── file1.txt
│   ├── file2.txt
│   └── ...
│
└── docker-compose.yml
```

* PServer: Contiene el servidor PServer implementado en Python con FastAPI.
* PClient: Contiene el cliente PClient implementado en Python con FastAPI y Jinja.
* CentralServer: Contiene el servidor central CentralServer implementado en Python con FastAPI.
* EroProxy: Contiene el proxy implementado en .NET con YARP.
* files: Directorio para almacenar archivos compartidos.
* docker-compose.yml: Archivo de configuración de Docker Compose para orquestar los servicios.

## Video explicativo del proceso de diseño, desarrollo y ejecución del programa.

[Video](https://youtu.be/40CItPiv-5k)

## Otra información que considere relevante para esta actividad.

### Referencias:

* [Proxy](https://www.tokioschool.com/noticias/que-es-proxy/)
* [Docker install](https://docs.docker.com/engine/install/ubuntu/)
* [Docker Swarm](https://docs.docker.com/engine/swarm/)
* [P2P sharing](https://github.com/Ezi0aaudit0re/P2P-music-sharing)
* [gRPC](https://grpc.io/docs/languages/python/basics/)
