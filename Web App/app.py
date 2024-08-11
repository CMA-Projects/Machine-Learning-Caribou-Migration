from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import joblib 

app = Flask(__name__)

# Load the model
model = joblib.load('models/DT_Model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Properly parse JSON
        month = float(data.get('month'))
        temperature = float(data.get('temperature'))
        day = float(data.get('day'))

        # Prepare the input for the model
        input_data = np.array([[month, temperature, day]])

        # Make prediction
        prediction = model.predict(input_data)

        # Format the prediction result
        result = {
            'latitude': prediction[0][0]  # Assumes the output is a 2D array with one value
        }

        return jsonify(result)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred during prediction'}), 400

if __name__ == '__main__':
    app.run(debug=True)
