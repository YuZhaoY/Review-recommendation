from flask import Blueprint
most_fivestars_bp = Blueprint('most_fivestars_bp', __name__)
from flasky.app.api.most_fivestars import routes