from fastapi import FastAPI, Request
import pickle
import numpy as np
from backend.basemodel import IrisRequest
import pandas as pd

app=FastAPI(title="ML e2e application")
model=pickle.load(open('model.pkl','rb'))
scalar=pickle.load(open('scaler.pkl','rb'))

@app.get("/")
def read_root():
    return  

@app.post("/predict")
def predict(request: IrisRequest):
    d=request.data
    data_df = pd.DataFrame([[
    d.sepal_length, d.sepal_width, d.petal_length, d.petal_width]], columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    scaled_data=scalar.transform(data_df)
    output=model.predict(scaled_data)
    return {'prediction': int(output[0])}
