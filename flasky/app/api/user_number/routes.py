from flask import request
from flask_jwt_extended import create_access_token
from flasky.app.api import db
from flasky.app.api.user_number import user_number_bp
from flasky.app.api.user_number.models import UserNumber
from flasky.app.api.user_number.schema import UserNumberSchema
from flasky.app.api.utils.responses import response_with
from flasky.app.api.utils import responses as resp
from flask_jwt_extended import jwt_required


@user_number_bp.route('/getNumber', methods=['GET'])
def getAllRecords():
    try:
        fetched = UserNumber.query.all()
        userNumberSchema = UserNumberSchema(many=True)
        userNumber = userNumberSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"userNumber": userNumber})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)