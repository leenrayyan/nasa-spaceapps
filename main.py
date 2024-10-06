from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model import load_trained_model, make_prediction  # Import model functions

# Initialize FastAPI app
app = FastAPI()

# Enable CORS to allow frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your website URL if needed for better security, e.g., ["https://your-website.com"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your pre-trained model
model = load_trained_model()

# Define a route to handle form submission and make predictions
@app.post("/predict")
async def predict(request: Request):
    try:
        # Parse the incoming JSON data
        data = await request.json()
        year = data['year']
        region = data['region']
        
        # Ensure the incoming data is in the correct format
        if not isinstance(year, int) or not isinstance(region, str):
            return {"error": "Invalid input format"}

        # Prepare the input dictionary
        input_data_dict = {"year": year, "region": region}

        # Make the prediction using the model
        prediction = make_prediction(model, input_data_dict)

        # Return the prediction as a JSON response
        return {"prediction": prediction}
    
    except Exception as e:
        return {"error": str(e)}  # Catch and return any error
