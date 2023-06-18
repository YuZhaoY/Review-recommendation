from flask import Blueprint
most_category_bp = Blueprint('most_category_bp', __name__)
from flasky.app.api.most_category import routes