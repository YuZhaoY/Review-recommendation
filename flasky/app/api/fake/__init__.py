from flask import Blueprint
fake_bp = Blueprint('fake_bp', __name__)
from flasky.app.api.fake import routes