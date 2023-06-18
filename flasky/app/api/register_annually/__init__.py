from flask import Blueprint
register_annually_bp = Blueprint('register_annually_bp', __name__)
from flasky.app.api.register_annually import routes