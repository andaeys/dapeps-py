from flask import jsonify
from app import app
from app.models import User


@app.route('/hello', methods=['GET'])
def sample_endpoint():
    data = {'message': 'This is a sample endpoint.'}
    return jsonify(data)


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': user_list})
