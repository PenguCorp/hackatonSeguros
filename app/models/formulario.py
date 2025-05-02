# formulario.py

from sqlalchemy import Column, Integer, String, Boolean, Enum, Text
from app.database import Base
import enum

class PlazoObjetivoEnum(str, enum.Enum):
    MENOS_3 = "menos_3"
    ENTRE_3_5 = "entre_3_5"
    MAS_5 = "mas_5"

class FrecuenciaActualizacionesEnum(str, enum.Enum):
    DIARIO = "diario"
    SEMANAL = "semanal"
    QUINCENAL = "quincenal"
    MENSUAL = "mensual"

class FrecuenciaPagosEnum(str, enum.Enum):
    SIEMPRE = "siempre"
    ALGUNAS_VECES = "algunas_veces"
    NUNCA = "nunca"

class ComodidadDigitalEnum(str, enum.Enum):
    MUY_COMODO = "muy_comodo"
    ALGO_COMODO = "algo_comodo"
    PREFIERO_HUMANO = "prefiero_humano"

class CaracterizacionUsuario(Base):
    __tablename__ = "caracterizacion_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)  # FK opcional si relacionas con 'usuarios'

    motivacion = Column(Text)
    plazo_objetivo = Column(Enum(PlazoObjetivoEnum))
    emocion_logro = Column(String)
    importancia = Column(Integer)

    frecuencia_actualizaciones = Column(Enum(FrecuenciaActualizacionesEnum))
    ayuda_recordatorios = Column(Boolean, default=False)
    ayuda_consejos = Column(Boolean, default=False)
    ayuda_explicaciones = Column(Boolean, default=False)
    ayuda_mensajes_importantes = Column(Boolean, default=False)

    tiene_otros_ahorros = Column(Boolean)
    frecuencia_pagos = Column(Enum(FrecuenciaPagosEnum))
    comodidad_digital = Column(Enum(ComodidadDigitalEnum))
