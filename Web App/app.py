from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

try:
    print("Model loading...")
    model = tf.keras.models.load_model('models/NN_3features_predict_lat.h5')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.json
        
        # Extract the input values
        input_values = data.get('inputs')
        
        # Check if the input values have exactly 3 elements
        if not input_values or len(input_values) != 3:
            return jsonify({'error': 'Input must be a list of 3 numerical values'}), 400
        
        # Convert the input values to a 2D numpy array
        input_array = np.array([input_values])
        
        # Make the prediction
        prediction = model.predict(input_array)
        
        # Extract the output from the 2D array and convert to standard Python float
        output_value = float(prediction[0][0])
        
        # Return the result as JSON
        return jsonify({'prediction': output_value})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'An error occurred during prediction'}), 500

if __name__ == '__main__':
    app.run(debug=True)
