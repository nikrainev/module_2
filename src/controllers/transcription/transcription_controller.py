from flask import Blueprint, jsonify, request, send_from_directory

from src.common.utils import expect
from src.controllers.auth.auth_service import create_user_service, check_auth

from flask_cors import CORS

from src.controllers.transcription.transcription_service import create_transcription_service
from src.datasource.category_repository import find_category_by_id

transcription_api = Blueprint(
    'transcription_api', 'transcription_api', url_prefix='/api/v1/transcriptions')

CORS(transcription_api)

@transcription_api.route('/transcription', methods=['POST'])
def tr():
    try:
        args = request.args
        token = expect(args.get('token'), str, 'args')

        check_auth(token)

        name = request.form['name']
        category_id = request.form['category_id']

        category = find_category_by_id(category_id)

        if (len(category) == 0):
            raise Exception("Category not found")

        if (str(category[0]['ownerUser']) != str(token)):
            raise Exception("Category not owned by me")

        file = request.files['file']

        result = create_transcription_service(
            file,
            name = name,
            owner_user_id = token,
            category_id = category_id
        )

        return jsonify({
            'text': result
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@transcription_api.route('/transcription/files/<path:path>')
def send_report(path):
    return send_from_directory('static/audio_files', path)