import pandas as pd
from app.etl.loader import insert_gastos

def process_csv(df: pd.DataFrame) -> int:
    df.columns = df.columns.str.strip().str.lower()
    
    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    df.dropna(subset=['data', 'valor'], inplace=True)

    df['categoria'] = df['categoria'].str.strip().str.title()
    df['tipo'] = df['tipo'].str.capitalize()

    insert_gastos(df)
    return len(df)


