#  API Mock Server - FastAPI

Este proyecto implementa una API REST con FastAPI que permite configurar y gestionar endpoints mockeados. Ideal para simular servicios externos durante pruebas o desarrollo.


##  Instalacion y ejecucion
Ejecutar desde la terminal e ir a la direccion obtenida
### Requisitos

- Python 3.9 o superior

### Instalacion

1. Clona el repositorio o descarga los archivos:

git clone https://github.com/Pabloo-Zam/API_challengeTigo
cd api-mock-server


### Ejemplo de configuración y solicitudes 
### ir a http://127.0.0.1:8000/docs
### copiar en POST/ configure mock
{
  "path": "/saludo",
  "method": "GET",
  "status_code": 200,
  "response_content": "{\"mensaje\": \"Hola Mundo\"}",
  "content_type": "application/json"
}

### en el navegador prueba
http://127.0.0.1:8000/saludo

