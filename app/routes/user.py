from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.models.user import fake_user_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    if user.username in fake_user_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    
    fake_user_db[user.username] = user.dict()
    return user

@router.get("/{username}", response_model=UserResponse)
def read_user(username: str):
    user = fake_user_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return user
