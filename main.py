from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import load_trained_model, make_prediction  # Your model-related imports

# Initialize FastAPI app
app = FastAPI()

# Enable CORS to allow frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your website URL for better security, e.g. ["https://your-website.com"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your pre-trained model
model = load_trained_model()

# Define a route to handle form submission and make predictions
@app.get("/predict")
async def predict(year: int, region: str):
    # Create the input dictionary
    input_data_dict = {"year": year, "region": region}
    
    # Get prediction from the model
    prediction = make_prediction(model, input_data_dict)

    # Return the prediction in JSON format
    return {"prediction": prediction}
