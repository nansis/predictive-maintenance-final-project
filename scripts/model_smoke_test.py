from huggingface_hub import hf_hub_download
import pandas as pd
import joblib

model_repo_id = "nansri/engine-predictive-maintenance-model"

model_path = hf_hub_download(
    repo_id=model_repo_id,
    filename="best_model.joblib",
    repo_type="model"
)

model = joblib.load(model_path)

sample_input = pd.DataFrame([{
    "Engine_rpm": 850,
    "Lub_oil_pressure": 3.5,
    "Fuel_pressure": 6.8,
    "Coolant_pressure": 2.4,
    "lub_oil_temp": 78.0,
    "Coolant_temp": 80.5
}])

prediction = model.predict(sample_input)[0]

print("Model smoke test completed successfully.")
print("Prediction:", prediction)