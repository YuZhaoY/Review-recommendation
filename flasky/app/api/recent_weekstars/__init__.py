from flask import Blueprint
recent_weekstars_bp = Blueprint('recent_weekstars_bp', __name__)
from flasky.app.api.recent_weekstars import routes