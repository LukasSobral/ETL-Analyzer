from pydantic import BaseModel
from datetime import date

class GastoCreate(BaseModel):
    data: date
    categoria: str
    descricao: str
    valor: float
    tipo: str
    forma_pagamento: str
