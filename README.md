
# Chatbot Claude - Proyecto de Integración de FastAPI con AWS Bedrock

Este proyecto es una API basada en **FastAPI** que utiliza **AWS Bedrock** para generar respuestas basadas en *prompts* de entrada. La arquitectura sigue el patrón de **Clean Architecture** y está contenida dentro de un entorno Docker para facilitar su despliegue y ejecución.

## Características del Proyecto

- **API REST** construida con **FastAPI**.
- **Integración con AWS Bedrock** para generación de texto usando el modelo **Claude v2**.
- Estructura del proyecto basada en **Clean Architecture**.
- Desplegable mediante **Docker**.
- Soporte para enviar *prompts* y obtener respuestas generadas por IA.

## Prerrequisitos

Asegúrate de tener instalados los siguientes componentes en tu sistema:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configuración de Variables de Entorno

El archivo `docker-compose.yml` requiere las siguientes variables de entorno para funcionar correctamente:

```bash
AWS_ACCESS_KEY_ID=tu_access_key
AWS_SECRET_ACCESS_KEY=tu_secret_access_key
DATABASE_URL="postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
```

Modifica estas variables con tus credenciales antes de ejecutar los contenedores.

## Instrucciones para Ejecutar el Proyecto

Sigue los siguientes pasos para ejecutar la API utilizando Docker:

1. **Clona el Repositorio**

   ```bash
   git clone https://github.com/paulmrg-461/bedrock_chatbot.git
   cd bedrock_chatbot
   ```

2. **Construye y Ejecuta el Contenedor**

   Utiliza `docker-compose` para construir y levantar los servicios:

   ```bash
   sudo docker-compose up --build
   ```

   Esto descargará las dependencias, construirá las imágenes Docker, y levantará el contenedor con la API.

3. **Accede a la API**

   La API estará disponible en la siguiente dirección:

   ```
   http://localhost:1724
   ```

## Uso de la API

Una vez que la API está corriendo, puedes realizar solicitudes para enviar *prompts* y obtener respuestas de AWS Bedrock.

### Endpoint para Enviar Prompts

- **URL**: `/generate-response`
- **Método**: `POST`
- **Descripción**: Este endpoint recibe un *prompt* y retorna la respuesta generada por el modelo Claude v2 desde AWS Bedrock.

### Ejemplo de Solicitud

Haz una solicitud `POST` utilizando herramientas como `curl`, Postman, o cualquier cliente HTTP.

```bash
curl -X POST "http://localhost:1724/generate-response" \
    -H "Content-Type: application/json" \
    -d '{"prompt": "¿Cómo fue el índice de calidad del aire en Popayán en 2022?"}'
```

### Ejemplo de Respuesta

```json
{
    "response": "El índice de calidad del aire en Popayán en 2022 fue bueno en general..."
}
```

## Documentación de la API

Puedes acceder a la documentación interactiva generada automáticamente por **Swagger** en:

```
http://localhost:1724/docs
```

Esta documentación te permitirá explorar y probar los distintos endpoints de la API de manera interactiva.

## Contribuciones

Si quieres contribuir a este proyecto, no dudes en hacer *pull requests* o reportar problemas en el repositorio.

---

**Developed by**: Paul Realpe