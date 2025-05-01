from sqlalchemy.orm import Session
from app.models import Gasto
from app.database import SessionLocal

def insert_gastos(df):
    db: Session = SessionLocal()
    for _, row in df.iterrows():
        gasto = Gasto(
            data=row['data'],
            categoria=row['categoria'],
            descricao=row.get('descricao', ''),
            valor=row['valor'],
            tipo=row['tipo'],
            forma_pagamento=row.get('forma_pagamento', '')
        )
        db.add(gasto)
    db.commit()
    db.close()
