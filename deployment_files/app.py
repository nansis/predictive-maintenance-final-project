
import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

st.set_page_config(page_title="Predictive Maintenance App", layout="centered")

MODEL_REPO_ID = "nansri/engine-predictive-maintenance-model"

@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id=MODEL_REPO_ID,
        filename="best_model.joblib",
        repo_type="model"
    )
    return joblib.load(model_path)

model = load_model()

st.title("Predictive Maintenance for Engine Health")
st.write("Enter the engine sensor values below to predict engine condition.")

engine_rpm = st.number_input("Engine RPM", min_value=0.0, value=850.0)
lub_oil_pressure = st.number_input("Lub Oil Pressure", min_value=0.0, value=3.5)
fuel_pressure = st.number_input("Fuel Pressure", min_value=0.0, value=6.8)
coolant_pressure = st.number_input("Coolant Pressure", min_value=0.0, value=2.4)
lub_oil_temp = st.number_input("Lub Oil Temperature", min_value=0.0, value=78.0)
coolant_temp = st.number_input("Coolant Temperature", min_value=0.0, value=80.5)

if st.button("Predict Engine Condition"):
    input_df = pd.DataFrame([{
        "Engine_rpm": engine_rpm,
        "Lub_oil_pressure": lub_oil_pressure,
        "Fuel_pressure": fuel_pressure,
        "Coolant_pressure": coolant_pressure,
        "lub_oil_temp": lub_oil_temp,
        "Coolant_temp": coolant_temp
    }])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("Prediction: Engine may require maintenance.")
    else:
        st.success("Prediction: Engine appears to be operating normally.")

    st.write("Input dataframe used for prediction:")
    st.dataframe(input_df)
