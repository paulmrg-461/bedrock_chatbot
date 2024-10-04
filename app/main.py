from fastapi import FastAPI
from app.api.controllers import router as api_router

app = FastAPI()

# Incluir las rutas de la API
app.include_router(api_router)