from flask import Blueprint
user_number_bp = Blueprint('user_number_bp', __name__)
from flasky.app.api.user_number import routes