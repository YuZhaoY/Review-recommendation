from flask import Blueprint
review_number_bp = Blueprint('review_number_bp', __name__)
from flasky.app.api.review_number import routes