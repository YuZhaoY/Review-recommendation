from flask import Blueprint
critic_bp = Blueprint('critic_bp', __name__)
from flasky.app.api.critic import routes