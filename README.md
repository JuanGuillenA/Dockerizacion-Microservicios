# Dockerizacion-Microservicios 
Este repositorio contiene un ejemplo de cómo dockerizar un microservicio y conectarlo con una base de datos PostgreSQL utilizando Docker y Docker Compose.
El proyecto levanta dos contenedores principales:<br>
Servicio API (FastAPI + Uvicorn)
Servicio DB (PostgreSQL 16)
<img width="784" height="122" alt="Captura de pantalla 2025-11-17 a la(s) 5 09 03 p  m" src="https://github.com/user-attachments/assets/6a1f33ad-53c3-4125-a05a-5091220459c8" />

Ambos se ejecutan dentro de una misma red interna creada por Docker Compose.
## Estructura del Proyecto
<img width="303" height="160" alt="Captura de pantalla 2025-11-17 a la(s) 5 10 57 p  m" src="https://github.com/user-attachments/assets/90415f42-07a4-4f55-b285-2dcd29d48486" />

## ¿Cómo se creó este proyecto?
Se creó la carpeta api/ con: <br>
main.py <br>
requirements.txt <br>
Dockerfile <br>
Se construyó el archivo docker-compose.yml para levantar simultáneamente: <br>
La API <br>
La base de datos PostgreSQL <br>
Se agregaron: <br>
Un volumen persistente para la BD <br>
Una red interna para conectar ambos servicios <br>
Healthchecks para validar el estado de los contenedores <br>
Archivo .env para una configuración flexible <br>

## Explicación de cada archivo
1) docker-compose.yml: <br>
Es el archivo que orquesta los dos contenedores (API y Base de Datos).
Define: <br>
Construcción de la API desde /api/Dockerfile <br>
Configuración de las variables de entorno <br>
Conexión a la base de datos <br>
Healthchecks para ambos servicios <br>
Red interna appnet <br>
<img width="721" height="810" alt="Captura de pantalla 2025-11-17 a la(s) 5 11 42 p  m" src="https://github.com/user-attachments/assets/0aa9643c-5830-40ed-8fe3-9a85993154e6" />

2) Carpeta /api: <br>
Contiene todo el código del microservicio FastAPI y su configuración. <br>
3) Dockerfile (dentro de /api) <br>
Define los pasos para construir la imagen del microservicio: <br>
Selección de imagen base Python <br>
Instalación de dependencias desde requirements.txt <br>
Copia del código fuente <br>
Exposición del puerto correspondiente <br>
Ejecución automática del servidor FastAPI con Uvicorn <br>
<img width="602" height="359" alt="Captura de pantalla 2025-11-17 a la(s) 5 12 02 p  m" src="https://github.com/user-attachments/assets/e0cc8511-e7d3-499e-af7b-bb708cf927d4" />

4) requirements.txt: <br>
Este archivo contiene todas las dependencias del microservicio, entre ellas: <br>
fastapi<br> 
uvicorn <br>
psycopg[binary] <br>
<img width="242" height="123" alt="Captura de pantalla 2025-11-17 a la(s) 5 12 16 p  m" src="https://github.com/user-attachments/assets/5d710927-3e82-47b1-9262-47ca8aed95a7" />

5) main.py: <br>
Archivo principal del microservicio: <br>
Crea la instancia de FastAPI <br>
Define las rutas y controladores <br>
Gestiona la conexión con PostgreSQL <br>
Incluye los endpoints <br>
/users: Devuelve una vista HTML con el listado completo de usuarios almacenados en PostgreSQL. <br>
/health:usado para mirar el estatus del docker. <br>
/health-ui: mismo healthcheck pero con diseño hecho por mi mismo. <br>
Y los botones tienen metodos post pero no se miran con el localhost. <br>
<img width="1161" height="805" alt="Captura de pantalla 2025-11-17 a la(s) 5 12 45 p  m" src="https://github.com/user-attachments/assets/97c98c72-8659-46e1-8866-35523f51171a" />

6) Archivo .env: <br>
Este archivo contiene las variables de entorno utilizadas por docker-compose.yml, y permite configurar fácilmente la API y la base de datos sin modificar el código. <br>
Ejemplo: <br>
## API
API_PORT=8000<br>

## DB
POSTGRES_DB=usersdbdbdb<br>
POSTGRES_USER=usersuseruser<br>
POSTGRES_PASSWORD=-------<br>
POSTGRES_PORT=5432<br>
Estas variables configuran:<br>
Puerto de la API<br>
Credenciales de PostgreSQL<br>
Nombre de la BD<br>
Puerto interno del servicio de base de datos<br>

## Cómo ejecutar este proyecto en cualquier lugar
- Requisitos: <br>
Tener instalado Docker <br>
Tener instalado Docker Compose (incluido en Docker Desktop) <br>
1) Clonar el repositorio: <br>
git clone https://github.com/JuanGuillenA/Dockerizacion-Microservicios.git <br>
cd Dockerizacion-Microservicios/compose-microservicio <br>
2) Verificar o editar el archivo .env: <br>
Ejemplo incluido: <br>
API_PORT=8000 <br>
POSTGRES_DB=usersdb <br>
POSTGRES_USER=usersuser <br>
POSTGRES_PASSWORD=supersecret <br>
POSTGRES_PORT=5432 <br>
Puedes modificarlo según tus necesidades. <br>
3) Levantar los servicios: <br>
docker compose up --build <br>
Esto: <br>
Construye la imagen de la API <br>
Descarga PostgreSQL <br>
Crea la red interna <br>
Ejecuta ambos servicios juntos <br>
<img width="692" height="497" alt="Captura de pantalla 2025-11-17 a la(s) 5 15 50 p  m" src="https://github.com/user-attachments/assets/f52fc9b2-caf9-4946-8468-6089c6b4063e" />

4) Probar la API: <br>
Abrir en el navegador: <br>
http://localhost:8000<br>
Healthcheck:<br>
http://localhost:8000/health<br>
<img width="1405" height="754" alt="Captura de pantalla 2025-11-17 a la(s) 5 18 27 p  m" src="https://github.com/user-attachments/assets/fa5cc1b2-5713-445e-af67-c69580d2eb9b" />

5) Detener todo:<br>
docker compose down<br>
Para borrar también el volumen:<br>
docker compose down -v<br>

## Resultado final
Con un solo comando (docker compose up) tendrás:<br>
Un microservicio corriendo con FastAPI <br>
Una base de datos PostgreSQL funcionando <br>
Conexión API ↔ DB completamente automatizada <br>
Persistencia de datos mediante volúmenes <br>
Entorno portable y fácil de replicar
