import streamlit as st
import requests
from backend.basemodel import IrisData, IrisRequest
import os

header=st.title("Hello, Streamlit!")

API_URL=os.getenv("API_URL","http://localhost:8000")

url = "http://127.0.0.1:8000/predict"

sepal_length=st.number_input("Sepal length")
sepal_width=st.number_input("Sepal width")
petal_length=st.number_input("Petal length")
petal_width=st.number_input("Petal width")

iris_data=IrisRequest(
    data=IrisData(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width
    ))

if st.button("Predict"):
    response=requests.post(f"{API_URL}/predict",json=iris_data.model_dump())

    try:
        if response.status_code==200:
            st.success(f"Prediction: {response.json()['prediction']}")
        else:
            st.error(f"Failed to predict{response.text}")
    except Exception as e:
        st.error(f"Error: {e}")