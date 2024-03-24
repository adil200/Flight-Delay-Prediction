from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pandas as pd

app = Flask(__name__)

# Loading the model and scaler
model = load_model('model.h5')
scaler = StandardScaler()

# Loading and preprocessing the training data
training_data = pd.read_csv('/Users/adilmohammed/Desktop/Flight Delay Predictor/flight_delay_predict.csv')  
X_train = training_data[['AirTime', 'Distance']]
scaler.fit(X_train)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        airtime = float(request.form['airtime'])
        distance = float(request.form['distance'])
        
        # Preprocessing user input
        user_input = np.array([[airtime, distance]])
        user_input_scaled = scaler.transform(user_input)
        
        # Predicting using the model
        predictions = model.predict(user_input_scaled)
        
        # Checking if the flight is delayed
        if predictions[0][1] >= 0.5:
            result = f"The flight is delayed by {predictions[0][0]} minutes."
        else:
            result = "The flight is not delayed."
        
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)