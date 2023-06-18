from flask import Blueprint
best_category_bp = Blueprint('best_category_bp', __name__)
from flasky.app.api.best_category import routes