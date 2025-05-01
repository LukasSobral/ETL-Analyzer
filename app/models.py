from app.database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    categoria = Column(String, nullable=False)
    descricao = Column(String)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)
    forma_pagamento = Column(String)
