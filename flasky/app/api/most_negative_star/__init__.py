from flask import Blueprint
most_negative_star_bp = Blueprint('most_negative_star_bp', __name__)
from flasky.app.api.most_negative_star import routes