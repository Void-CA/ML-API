# app.py
from flask import Flask, request, jsonify, send_from_directory
import pickle
import numpy as np
import os

app = Flask(__name__)

# Cargar el modelo
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Mapa de números de clase a nombres de clase y URLs de imágenes
class_info = {
    0: {'name': 'iris-setosa', 'image': '/static/images/iris_setosa.jpeg'},
    1: {'name': 'iris-versicolor', 'image': '/static/images/iris_versicolor.jpeg'},
    2: {'name': 'iris-virginica', 'image': '/static/images/iris_virginica.jpeg'}
}

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        predicted_class = int(prediction[0])
        predicted_info = class_info.get(predicted_class, {'name': 'Unknown', 'image': ''})
        return jsonify({'prediction': predicted_info})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
