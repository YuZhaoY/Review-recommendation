from flask import Blueprint
categories_number_bp = Blueprint('categories_number_bp', __name__)
from flasky.app.api.categories_numbers import routes