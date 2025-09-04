import streamlit as st
import requests
from basemodel import IrisData, IrisRequest

header=st.title("Hello, Streamlit!")

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
    response=requests.post(url,json=iris_data.model_dump())

    try:
        if response.status_code==200:
            st.success(f"Prediction: {response.json()['prediction']}")
        else:
            st.error(f"Failed to predict{response.text}")
    except Exception as e:
        st.error(f"Error: {e}")