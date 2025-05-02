# schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class PlazoObjetivoEnum(str, Enum):
    MENOS_3 = "menos_3"
    ENTRE_3_5 = "entre_3_5"
    MAS_5 = "mas_5"

class FrecuenciaActualizacionesEnum(str, Enum):
    DIARIO = "diario"
    SEMANAL = "semanal"
    QUINCENAL = "quincenal"
    MENSUAL = "mensual"

class FrecuenciaPagosEnum(str, Enum):
    SIEMPRE = "siempre"
    ALGUNAS_VECES = "algunas_veces"
    NUNCA = "nunca"

class ComodidadDigitalEnum(str, Enum):
    MUY_COMODO = "muy_comodo"
    ALGO_COMODO = "algo_comodo"
    PREFIERO_HUMANO = "prefiero_humano"

class CaracterizacionRequest(BaseModel):
    usuario_id: int
    motivacion: Optional[str]
    plazo_objetivo: PlazoObjetivoEnum
    emocion_logro: Optional[str]
    importancia: int

    frecuencia_actualizaciones: FrecuenciaActualizacionesEnum
    ayuda_recordatorios: bool
    ayuda_consejos: bool
    ayuda_explicaciones: bool
    ayuda_mensajes_importantes: bool

    tiene_otros_ahorros: bool
    frecuencia_pagos: FrecuenciaPagosEnum
    comodidad_digital: ComodidadDigitalEnum
    class Config:
        orm_mode = True
