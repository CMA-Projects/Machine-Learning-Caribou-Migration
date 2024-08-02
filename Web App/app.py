from flask import Flask, request, jsonify
import tensorflow as tf

# Load the trained models
model_linear = tf.keras.models.load_model('Linear_Model.h5')
model_rf = tf.keras.models.load_model('RF_Model.h5')
model_svr = tf.keras.models.load_model('SVR_Model.h5')
model_knn = tf.keras.models.load_model('KNN_Model.h5')
model_gb = tf.keras.models.load_model('GB_Model.h5')
model_dt = tf.keras.models.load_model('DT_Model.h5')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    month = data['month']
    temperature = data['temperature']
    input_features = [[month, temperature]]

    predictions = {
        'linear': model_linear.predict(input_features)[0],
        'random_forest': model_linear.predict(input_features)[0],
        'svr': model_linear.predict(input_features)[0],
        'knn': model_linear.predict(input_features)[0],
        'gradient_boosting': model_linear.predict(input_features)[0],
        'decision_tree': model_linear.predict(input_features)[0],
    }

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)