from flask import Blueprint
nearby_search_bp = Blueprint('nearby_search_bp', __name__)
from flasky.app.api.nearby_search import routes