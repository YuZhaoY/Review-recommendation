from flask import Blueprint
word_count_bp = Blueprint('word_count_bp', __name__)
from flasky.app.api.word_count import routes