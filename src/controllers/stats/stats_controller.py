import requests
from flask import Blueprint
from jinja2 import Environment, FileSystemLoader, select_autoescape


stats_api = Blueprint(
    'stats_api', 'stats_api', url_prefix='/api/v1/stats')

env = Environment(
    loader=FileSystemLoader("templates/"),
    autoescape=select_autoescape()
)

template = env.get_template("template.txt")

UserElonMusk = {
    'name': 'Elon Musk',
    'transcriptionCount': 10,
    'categoriesCount': 52,
    'country': 'US',

    'name1': 'Nikita Krainev',
    'transcriptionCount1': 103,
    'categoriesCount1': 2,
    'country1': 'RU',
}

@stats_api.route("/users")
def nikita_page():
    return template.render(UserElonMusk)