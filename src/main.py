import os

from flask import Flask, render_template
from flask_cors import CORS

import json

from bson import json_util, ObjectId
from datetime import datetime

from src.controllers.auth.auth_controller import auth_api
from src.controllers.category.category_controller import category_api
from src.controllers.stats.stats_controller import stats_api
from src.controllers.transcription.transcription_controller import transcription_api


class MongoJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, 'build/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, 'build')

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                template_folder=TEMPLATE_FOLDER,
                )
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(auth_api)
    app.register_blueprint(category_api)
    app.register_blueprint(transcription_api)
    app.register_blueprint(stats_api)

    return app