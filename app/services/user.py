from sqlalchemy.orm import Session
from app.models.user import user
from app.services.auth import hash_password

def get_usuario(db: Session, usuario_id: int):
    return db.query(user).filter(user.id == usuario_id).first()

def get_usuario_by_email(db: Session, email: str):
    return db.query(user).filter(user.email == email).first()

def create_usuario(db: Session, nombre: str, email: str, password: str):
    hashed_pw = hash_password(password)
    db_usuario = user(nombre=nombre, email=email, hashed_password=hashed_pw)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
