from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.database import get_db
from app.services import user

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_usuario(usuario: UserCreate, db: Session = Depends(get_db)):
    return user.create_usuario(db=db, nombre=usuario.nombre, correo=usuario.correo)

@router.get("/{usuario_id}", response_model=UserResponse)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = user.get_usuario(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario
