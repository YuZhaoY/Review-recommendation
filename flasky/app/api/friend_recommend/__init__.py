from flask import Blueprint
friend_recommend_bp = Blueprint('friend_recommend_bp', __name__)
from flasky.app.api.friend_recommend import routes