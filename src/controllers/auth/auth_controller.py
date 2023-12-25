from flask import Blueprint, jsonify, request

from src.common.utils import expect
from src.controllers.auth.auth_service import create_user_service
from src.controllers.auth.request.create_user_request import CreateUserRequest

from flask_cors import CORS

auth_api = Blueprint(
    'auth_api', 'auth_api', url_prefix='/api/v1/auth')

CORS(auth_api)

@auth_api.route('/me', methods=['POST'])
def createUser():
    try:
        post_data = request.get_json()

        print('in route')

        username = expect(post_data.get('username'), str, 'username')
        firstName = expect(post_data.get('firstName'), str, 'firstName')
        lastName = expect(post_data.get('lastName'), str, 'lastName')

        response = create_user_service(CreateUserRequest(username, firstName, lastName, request.remote_addr))

        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

