from flask import Blueprint
emotions_bp = Blueprint('emotions_bp', __name__)
from flasky.app.api.emotions import routes