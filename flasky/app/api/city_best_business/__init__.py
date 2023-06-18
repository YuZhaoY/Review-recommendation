from flask import Blueprint
city_best_business_bp = Blueprint('city_best_business_bp', __name__)
from flasky.app.api.city_best_business import routes