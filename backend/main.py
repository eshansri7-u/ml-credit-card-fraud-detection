from fastapi import FastAPI
import pandas as pd
import joblib
from schemas import transaction

app = FastAPI()

model = joblib.load("models/fraud_pipeline.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: transaction):
    df = pd.DataFrame([{
        "step": data.step,
        "type": data.types,
        "amount": data.amount
    }])
    prediction = model.predict(df)[0]
    if(prediction == 1):
        return {"prediction" : "fraudulant"}
    else:
        return {"prediction" :"not fraudulant"}
    



