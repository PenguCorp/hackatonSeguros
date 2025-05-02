from sqlalchemy.orm import Session
from app.models.formulario import CaracterizacionUsuario
from app.schemas.formulario import CaracterizacionRequest

def crear_caracterizacion(db: Session, data: CaracterizacionRequest):
    caracterizacion = CaracterizacionUsuario(
        usuario_id=data.usuario_id,
        motivacion=data.motivacion,
        plazo_objetivo=data.plazo_objetivo,
        emocion_logro=data.emocion_logro,
        importancia=data.importancia,
        frecuencia_actualizaciones=data.frecuencia_actualizaciones,
        ayuda_recordatorios=data.ayuda_recordatorios,
        ayuda_consejos=data.ayuda_consejos,
        ayuda_explicaciones=data.ayuda_explicaciones,
        ayuda_mensajes_importantes=data.ayuda_mensajes_importantes,
        tiene_otros_ahorros=data.tiene_otros_ahorros,
        frecuencia_pagos=data.frecuencia_pagos,
        comodidad_digital=data.comodidad_digital
    )
    db.add(caracterizacion)
    db.commit()
    db.refresh(caracterizacion)
    return caracterizacion
