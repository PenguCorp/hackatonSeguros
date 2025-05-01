from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import user as user_service
from app.services.auth import verify_password
from app.schemas.user import LoginRequest

router = APIRouter()


@router.post("/")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    db_user = user_service.get_usuario_by_email(db, login_data.correo)
    if not db_user or not verify_password(login_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Inicio de sesión exitoso", "user_id": db_user.id}
