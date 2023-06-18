from flask import Blueprint
most_business_bp = Blueprint('most_business_bp', __name__)
from flasky.app.api.most_business import routes