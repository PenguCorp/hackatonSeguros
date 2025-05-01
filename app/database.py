# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://hackatonDB_owner:npg_qCkVuYo5PJH7@ep-wandering-river-a4lhjos5-pooler.us-east-1.aws.neon.tech/hackatonDB?sslmode=require"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la clase base para los modelos
Base = declarative_base()

# Crear el objeto SessionLocal que se usará para crear sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()