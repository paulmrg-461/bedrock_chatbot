FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecutar el servidor Uvicorn para FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1724"]
