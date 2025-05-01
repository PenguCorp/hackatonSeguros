# crud.py
from sqlalchemy.orm import Session
from app.models.user import user

def get_usuario(db: Session, usuario_id: int):
    return db.query(user).filter(user.id == usuario_id).first()

def create_usuario(db: Session, nombre: str, correo: str):
    db_usuario = user(nombre=nombre, correo=correo)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
