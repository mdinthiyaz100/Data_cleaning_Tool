from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Data Cleaning API is running successfully!"}

@app.post("/clean")
async def clean_data(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    df = df.drop_duplicates()
    df = df.dropna()
    summary = df.describe(include='all')
    cleaned_csv = df.to_csv(index=False)
    return {
        "summary_report": summary.to_json(),
        "cleaned_data": cleaned_csv
    }





