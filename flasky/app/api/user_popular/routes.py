from flask import request
from flask_jwt_extended import create_access_token
from flasky.app.api import db
from flasky.app.api.user_popular import user_popular_bp
from flasky.app.api.user_popular.models import UserPopular
from flasky.app.api.user_popular.schema import UserPopularSchema
from flasky.app.api.utils.responses import response_with
from flasky.app.api.utils import responses as resp
from flask_jwt_extended import jwt_required


@user_popular_bp.route('/getPopular', methods=['GET'])
def getAllRecords():
    try:
        fetched = UserPopular.query.all()
        userPopularSchema = UserPopularSchema(many=True)
        userPopular = userPopularSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"userPopular": userPopular})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)