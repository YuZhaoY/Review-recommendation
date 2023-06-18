from flask import Blueprint
userrecs_bp = Blueprint('userrecs_bp', __name__)
from flasky.app.api.userrecs import routes