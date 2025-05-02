from fastapi import FastAPI
from app.routes import user, login
from app.database import engine, SessionLocal, Base
from fastapi.middleware.cors import CORSMiddleware


# Configurar CORS
origins = [
    "http://localhost:5173",  # URL del frontend de React
    "https://your-production-domain.com"  # Agrega otros dominios permitidos si es necesario
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(login.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}
