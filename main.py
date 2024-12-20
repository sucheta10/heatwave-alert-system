from data_preprocessing import load_data, preprocess_data
from model_training import train_model
from alert_system import send_alert
import pandas as pd
import pickle

# Step 1: Load and preprocess data
data_path = 'data/weather_data.csv'
data = load_data(data_path)
processed_data = preprocess_data(data)

# Step 2: Train the model
model = train_model(processed_data)

# Step 3: Predict and send alerts
new_data = pd.DataFrame({
    'Temperature': [0.9],  # Normalized value
    'Humidity': [0.8],     # Normalized value
    'Heat_Index': [0.85]   # Normalized value
})

# Load the model
with open('heatwave_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Predict
prediction = model.predict(new_data)[0]

# Send alert if heatwave is predicted
if prediction == 1:
    send_alert("Heatwave Alert: Stay indoors and hydrated!", "+11234567890")
