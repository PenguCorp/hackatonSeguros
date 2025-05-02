from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import user as user_service
from app.services.auth import verify_password
from app.schemas.user import LoginRequest
from app.services.authjwt import create_access_token

router = APIRouter()

@router.post("/")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    db_user = user_service.get_usuario_by_email(db, login_data.email)
    if not db_user or not verify_password(login_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_access_token(data={"sub": str(db_user.id)})
    return {"access_token": token, "user_id": db_user.id, "user_email": db_user.email}