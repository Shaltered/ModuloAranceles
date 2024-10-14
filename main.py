from fastapi import FastAPI
from database import engine
from models import Base
from routes import debts

app = FastAPI()

# Crear las tablas automáticamente
Base.metadata.create_all(bind=engine)

# Agregar las rutas
app.include_router(debts.router)

@app.get("/api/v1/health")
async def health_check():
    return {"status": "ok"}
