from flask import Blueprint
business_referrals_bp = Blueprint('business_referrals_bp', __name__)
from flasky.app.api.Business_Referrals import routes