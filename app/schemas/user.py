from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nombre: str
    correo: EmailStr

class UserCreate(UserBase):
    password: str  # Agregado

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str

