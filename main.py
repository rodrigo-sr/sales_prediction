from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np


app = FastAPI()

# Carregar os modelos
model_uk = joblib.load('models/model_uk.pkl')
model_fr = joblib.load('models/model_fr.pkl')
model_de = joblib.load('models/model_de.pkl')
model_eire = joblib.load('models/model_eire.pkl')
model_others = joblib.load('models/model_others.pkl')

# Carregar scaler
scaler = joblib.load('models/scaler.pkl')

# Dicionário para mapear os modelos
models = {
    'United Kingdom': model_uk,
    'France': model_fr,
    'Germany': model_de,
    'EIRE': model_eire,
    'Others': model_others
}

# Classe para o corpo da requisição
class PredictionRequest(BaseModel):
    country: str
    month: int
    day_of_week_numeric: int

# Endpoint de saúde
@app.get("/")
def read_root():
    return {"message": "API is running"}

# Endpoint para previsão
@app.post("/predict/")
def predict(request: PredictionRequest):
    if request.country not in models:
        raise HTTPException(status_code=404, detail="Country model not found")
    
    model = models.get(request.country, models['Others'])
    
    # Dados de entrada
    input_data = pd.DataFrame([{
        'Month': request.month,
        'DayOfWeekNumeric': request.day_of_week_numeric
    }])
    
    # Fazer a previsão
    prediction = model.predict(input_data)
    
    prediction_inverse = scaler.inverse_transform(prediction.reshape(-1, 1))
    
    return {
        "country": request.country,
        "prediction": prediction_inverse[0][0] * 1000
    }
