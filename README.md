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


## 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Se utilizaron las siguientes tecnologías y prácticas:

* Arquitectura cliente-servidor.
* Implementación de servidor central utilizando FastAPI en Python 3.11.1.
* Implementación de servidor de descargas utilizando gRPC.
* Interfaz gráfica de cliente desarrollada con Jinja y FastAPI.
* Implementación de un proxy en .NET utilizando YARP para redirigir las peticiones a los diferentes servidores.

![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/d886c07c-1ef9-40ed-bfc9-f8e4c79f0a9f)

## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
* Lenguaje de programación: Python 3.11.1, .NET
* Librerías y paquetes utilizados:
    * FastAPI
    * gRPC
    * Jinja
    * YARP

## Cómo se compila y ejecuta.
Hacerle git clone a este repositorio:
```bash
git clone https://github.com/dgonzalezt2/dgonzalez2-st0263.git
```
Ubicarse en .\ServerCentral\ y ejecutar:
```bash
pip install -r requirements.txt
```
Posteriormente ubicarse en .\Peer\p-client\ y ejecutar:
```bash
py program.py   
```
```bash
py main.py
```
Para ejecutar el docker se realiza lo siguiente
```bash
npm start
```
```bash
docker compose up
```

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

* PServer: Contiene el servidor PServer implementado en Python 3.11.1 con FastAPI.
* PClient: Contiene el cliente PClient implementado en Python 3.11.1 con FastAPI y Jinja.
* CentralServer: Contiene el servidor central CentralServer implementado en Python 3.11.1 con FastAPI.
* EroProxy: Contiene el proxy implementado en .NET con YARP.
* files: Directorio para almacenar archivos compartidos.
* docker-compose.yml: Archivo de configuración de Docker Compose para orquestar los servicios.

## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Las máquinas virtuales de Ubuntu en AWS se utilizan para desplegar los servicios. Cada máquina tiene asignada una IP elástica para mantener la consistencia de las direcciones IP entre diferentes sesiones.
## IP o Nombres de Dominio en la Nube o en la Máquina Servidor
* http://54.226.116.91/
* http://44.220.139.100/
## Como se lanza el servidor.
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/335cd8d1-c00f-4a4f-a9e6-57f80fd3b890)
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/b5300291-8d8c-4688-ab79-a54fcef3426e)
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/dd5a6afe-d038-42b6-975f-fef7b622d984)
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/cbc8ddb6-29a8-4a7c-a25c-9efc13213a55)
# Creamos nuestro EC2 con 3 instancias en total un central, peer1 y peer2
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/6b2425d4-28ac-49a9-a67e-f91f80aa0d19)
# Le damos arriba en lanzar instancias para crearlas teniendo estas especificaciones para los peers
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/7aeb2923-3215-4045-930f-2ef0b0031dbd)
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/cccc79d7-8c15-4f17-b098-09625c4d2dfd)
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/ff6dd8eb-2d28-48a3-8ea1-2c86cf08aa11)
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/d9377abe-96a2-472e-a04b-b2d3b9f5b8ed)

# Una vez creado las Instancias 
# Central
Abrimos una consola para poner comandos en 'Central' con el siguiente comando:
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/c1a8f6a1-91a6-49c3-b746-da9563b7aea7)
Posteriormente se instala docker una vez instalado el anterior comando
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```bash
sudo docker run hello-world
```
Posteriormente se clona el repositorio
```bash
git clone https://github.com/dgonzalezt2/dgonzalez2-st0263.git
```
Nos ubicamos en nuestro documento clonado
```bash
cd dgonzalez2-st0263/
```
Y añademos el siguiente comando
```bash
sudo docker compose -f docker-compose-central.yaml up -d
```
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/d319c698-28c8-422a-ba7e-5158e1b7a028)
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/7538a9cc-129f-4465-ae84-a6424160e1ff)

# Peer 1
Abrimos otra consola para poner los comandos del 'Peer1' con el siguiente comando:
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/56462ce1-74f5-4d9a-bb92-8c374f232be4)
Posteriormente se instala docker una vez instalado el anterior comando
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```bash
sudo docker run hello-world
```
Posteriormente se clona el repositorio
```bash
git clone https://github.com/dgonzalezt2/dgonzalez2-st0263.git
```
Nos ubicamos en nuestro documento clonado
```bash
cd dgonzalez2-st0263/
```
Ejecutamos el docker
```bash
sudo docker compose up -d
```
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/46ad430f-3119-4ce4-a657-ed626300889c)

# Peer 2
Abrimos otra consola para poner los comandos del 'Peer2' con el comando que nos proporciona la instancia:
Posteriormente se instala docker una vez instalado el anterior comando
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```bash
sudo docker run hello-world
```
Posteriormente se clona el repositorio
```bash
git clone https://github.com/dgonzalezt2/dgonzalez2-st0263.git
```
Nos ubicamos en nuestro documento clonado
```bash
cd dgonzalez2-st0263/
```
Ejecutamos el docker
```bash
sudo docker compose up -d
```
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/791fa4d5-9f47-47d0-8071-3980d79f04c2)

## Para ver las paginas web desplegada en AWS las puedes encontrar en los siguientes links.

* Peer1: http://54.226.116.91/
* Peer2: http://44.220.139.100/

![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/8d11a939-5a37-4a69-9a7f-725b69401651)

## Mini Guía de Uso para el Usuario
Seleccionar alguno de los 2 IP:
[IP_1](http://54.226.116.91/)
[IP_2](http://44.220.139.100/)
* Le das en Seleccionar Archivo en la parte posterior izquierda, una vez cargado el programa le das en subir esperas unos segundos y te notifica que ya subio el archivo, te regresas a la pagina principal y ya puedes apreciar el archivo subido en la IP seleccionada.
* Al darle click en cualquier archivo se descarga.
![image](https://github.com/dgonzalezt2/dgonzalez2-st0263/assets/81880494/0d832e3e-da2d-4ab7-b9b9-cc16d90bbfb3)

## Video explicativo del proceso de diseño, desarrollo y ejecución del programa.

[Video](https://youtu.be/40CItPiv-5k)

### Referencias:

* [Proxy](https://www.tokioschool.com/noticias/que-es-proxy/)
* [Docker install](https://docs.docker.com/engine/install/ubuntu/)
* [Docker Swarm](https://docs.docker.com/engine/swarm/)
* [P2P sharing](https://github.com/Ezi0aaudit0re/P2P-music-sharing)
* [gRPC](https://grpc.io/docs/languages/python/basics/)
