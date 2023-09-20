from flask import request, jsonify
from app import app
from app.models import User
from tensorflow.keras.models import load_model
import numpy as np
import logging

MODEL_FILE_PATH = 'pretrainec_1.h5'

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


@app.route('/hello', methods=['GET'])
def sample_endpoint():
    data = {'message': 'This is a sample endpoint.'}
    return jsonify(data)


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': user_list})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the pre-trained model
        model = load_model(MODEL_FILE_PATH)

        # Get the input data from the request
        input_data = request.json

        logging.info(f"anda_debug, json input: {input_data}")
        in_data = input_data['input_data']

        # Validate input data
        if not isinstance(in_data, list) or len(in_data) != 5:
            return jsonify({'error': 'Invalid input. Please provide a list of 5 integers (0, 1, or 2).'}), 400

        input_data = np.array(in_data)

        # Make the prediction
        prediction = model.predict(np.expand_dims(input_data, axis=0))

        return jsonify({'prediction': prediction[0].tolist()})

    except Exception as e:
        logging.info(f"error: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

    # return jsonify({'error': 'Model loading failed.'}), 500

