from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.database import get_db
from app.services import user as user_service
from app.models.user import user


router = APIRouter()

@router.get("/{usuario_id}", response_model=UserResponse)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = user_service.get_usuario(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.post("/", response_model=UserResponse)
def create_usuario(usuario: UserCreate, db: Session = Depends(get_db)):
    existing_user = user_service.get_usuario_by_email(db, usuario.correo)
    if existing_user:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    return user_service.create_usuario(
        db=db, nombre=usuario.nombre, correo=usuario.correo, password=usuario.password
    )
