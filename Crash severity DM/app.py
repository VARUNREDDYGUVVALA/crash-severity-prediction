from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('random_forest_top10.pkl')
scaler = joblib.load('scaler_top10.pkl')
top_features = joblib.load('top10_features.pkl')  # Optional but helps ordering

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input features
        input_data = [request.form[feature] for feature in top_features]
        input_data = np.array(input_data, dtype=float).reshape(1, -1)

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)[0]

        return render_template('index.html', prediction=f'Predicted Crash Type: {prediction}')
    except Exception as e:
        return render_template('index.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
