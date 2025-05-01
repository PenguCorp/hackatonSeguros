# models.py
from sqlalchemy import Column, Integer, String
from app.database import Base


class user(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo = Column(String, unique=True, index=True)

fake_user_db = {}