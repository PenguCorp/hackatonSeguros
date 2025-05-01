from sqlalchemy.orm import Session
from app.models.user import user
from app.services.auth import hash_password

def get_usuario(db: Session, usuario_id: int):
    return db.query(user).filter(user.id == usuario_id).first()

def get_usuario_by_email(db: Session, correo: str):
    return db.query(user).filter(user.correo == correo).first()

def create_usuario(db: Session, nombre: str, correo: str, password: str):
    hashed_pw = hash_password(password)
    db_usuario = user(nombre=nombre, correo=correo, hashed_password=hashed_pw)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
