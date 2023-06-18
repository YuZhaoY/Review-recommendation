from flask import Blueprint
users_bp = Blueprint('users_bp', __name__)
from flasky.app.api.users import routes