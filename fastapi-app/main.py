from fastapi import FastAPI, Request  # Importing FastAPI and Request for POST data handling
import pickle
from pydantic import BaseModel

# Load your pre-trained model
model = pickle.load(open(r'modelgc.pkl', 'rb'))


# Create an instance of FastAPI
app = FastAPI()

# Define a Pydantic model to validate input data
class PredictionInput(BaseModel):
    age_years: float
    gender: float
    height: float
    weight: float
    ap_hi: float
    ap_lo: float
    cholesterol: float
    gluc: float
    smoke: float
    alco: float
    active: float
    Heart_r: float
    cardio: float

# Define the GET route (optional, as per your requirement)
@app.get("/hello")
def read_hello():
    return {"message": "Hello World! I am here update"}

# Define the POST route for making predictions
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Extract data from the request
    features = [
        input_data.age_years, input_data.gender, input_data.height, input_data.weight, 
        input_data.ap_hi, input_data.ap_lo, input_data.cholesterol, input_data.gluc,
        input_data.smoke, input_data.alco, input_data.active, input_data.Heart_r, input_data.cardio
    ]

    # Make prediction using the loaded model
    prediction = model.predict([features])

    # Categories for prediction results
    categories = ['Normal', 'Elevated', 'Hypertension Stage 1', 'Hypertension Stage 2']
    prediction_text = categories[int(prediction[0])]

    # Return the prediction result in JSON format
    return {"Predicted value": prediction_text}

