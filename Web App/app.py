from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model("models/DT_Model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', nethods=['POST'])
def predict():
    data = request.json
    month = data['month']
    temperature = data['temperature']
    day = data['day']

    input_data = np.array([[month, temperature, day]])
    prediction = model.predict(input_data)

    result = {
        'latitude': prediction[0][0]
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)