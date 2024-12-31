from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# Load the Pickle model
with open("ames_model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize FastAPI app
app = FastAPI()

# Input schema for prediction
class HouseData(BaseModel):
    features: list  # Input features as a list

@app.post("/predict/")
def predict(data: HouseData):
    # Convert features to NumPy array
    features = np.array(data.features).reshape(1, -1)
    
    # Check for invalid input size
    if features.shape[1] != model.n_features_in_:
        return {"error": "Invalid number of features provided."}

    # Make prediction
    prediction = model.predict(features)
    return {"prediction": prediction[0]}
