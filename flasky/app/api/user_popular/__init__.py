from flask import Blueprint
user_popular_bp = Blueprint('user_popular_bp', __name__)
from flasky.app.api.user_popular import routes