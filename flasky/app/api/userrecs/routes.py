from flask import request
from flask_jwt_extended import create_access_token
from flasky.app.api import db
from flasky.app.api.userrecs import userrecs_bp
from flasky.app.api.userrecs.models import Userrecs
from flasky.app.api.userrecs.schema import UserrecsSchema
from flasky.app.api.utils.responses import response_with
from flasky.app.api.utils import responses as resp
from flask_jwt_extended import jwt_required


@userrecs_bp.route('/getUserrecs', methods=['GET'])
def getAllRecords():
    try:
        fetched = Userrecs.query.all()
        userrecsSchema = UserrecsSchema(many=True)
        userrecs = userrecsSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"userrecs": userrecs})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)