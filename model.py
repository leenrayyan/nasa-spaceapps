from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np
from sklearn.preprocessing import StandardScaler

# Assuming you already have a model definition, you can recreate it
def load_trained_model():
    model = Sequential()
    model.add(Input(shape=(2,)))  # Modify based on your input shape
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=3, activation='softmax'))  # Modify based on the number of classes

    # Compile the model (same as you did during training)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Instead of loading from a .h5 file, we assume this is your trained model definition
    # You could also add the weights manually if needed

    return model

# Function to preprocess the input data
def preprocess_input(input_data):
    # Extract year and region from input_data
    year = input_data['year']
    region = input_data['region']

    # Example of how you may process year and region
    scaler = StandardScaler()
    year_scaled = scaler.fit_transform([[year]])[0][0]

    # Assuming region is encoded (label encoded or one-hot encoded)
    region_encoded = 0  # Add encoding logic for the region if needed

    # Combine the preprocessed features into a single array
    preprocessed_data = np.array([[year_scaled, region_encoded]])

    return preprocessed_data

def make_prediction(model, input_data):
    preprocessed_data = preprocess_input(input_data)
    prediction = model.predict(preprocessed_data)
    predicted_class = np.argmax(prediction, axis=1)[0]  # Extract the class number
    if predicted_class == 0:
        return 'Ice Melt, Sea Level Rise'
    elif predicted_class == 1:
        return 'Extreme Heat, Storms'
    else:
        return 'Ozone Depletion, Cooling Effects'
