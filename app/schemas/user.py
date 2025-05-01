# app/schemas.py (o donde tengas tus esquemas)
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    nombre: str
    correo: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    nombre: str
    correo: str

