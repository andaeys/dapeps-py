from flask import jsonify
from app import app


@app.route('/hello', methods=['GET'])
def sample_endpoint():
    data = {'message': 'This is a sample endpoint.'}
    return jsonify(data)