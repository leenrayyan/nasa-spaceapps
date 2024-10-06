from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model import load_trained_model, make_prediction  # Your model-related imports

# Initialize FastAPI app
app = FastAPI()

# Load your pre-trained model
model = load_trained_model()

# Set up Jinja2 templates (for rendering HTML)
templates = Jinja2Templates(directory="templates")

# Define a route to display the input form
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Define a route to handle form submission and make predictions
@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, year: int = Form(...), region: str = Form(...)):
    # Create the input dictionary
    input_data_dict = {"year": year, "region": region}
    
    # Get prediction from the model
    prediction = make_prediction(model, input_data_dict)

    # Return the prediction and render it on the result page
    return templates.TemplateResponse("result.html", {"request": request, "year": year, "region": region, "prediction": prediction})
