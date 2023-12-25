from flask import Blueprint, jsonify, request

from src.common.utils import expect
from src.controllers.auth.auth_service import  check_auth

from flask_cors import CORS

from src.controllers.category.category_service import create_category_service, get_my_categories_service

category_api = Blueprint(
    'categories_api', 'categories_api', url_prefix='/api/v1/categories')

CORS(category_api)

@category_api.route('/category', methods=['POST'])
def createCategory():
    try:
        post_data = request.get_json()
        args = request.args
        token = expect(args.get('token'), str, 'args')
        name = expect(post_data.get('name'), str, 'name')

        check_auth(token)

        create_category_service(name, token)

        return jsonify({
            'success': token
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@category_api.route('/me', methods=['GET'])
def get_my_categories():
    try:
        args = request.args
        token = expect(args.get('token'), str, 'args')

        result = get_my_categories_service(token)

        return jsonify({
            'success': result
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400