from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nombre: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  # Agregado

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

