from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.formulario import CaracterizacionRequest
from app.services import formulario as service

router = APIRouter()

@router.post("/")
def registrar_caracterizacion(data: CaracterizacionRequest, db: Session = Depends(get_db)):
    try:
        result = service.crear_caracterizacion(db, data)
        return {"message": "Formulario enviado con éxito", "id": result.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    