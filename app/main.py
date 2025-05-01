from fastapi import FastAPI
from app.routes import user
from app.database import engine, SessionLocal, Base
# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}
