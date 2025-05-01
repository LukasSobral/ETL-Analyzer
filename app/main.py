from fastapi import FastAPI, UploadFile, File
import pandas as pd
from app.etl.processor import process_csv

app = FastAPI()

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file, encoding="latin1", sep=";")

    linhas = process_csv(df)
    return {"message": f"{linhas} registros processados"}
