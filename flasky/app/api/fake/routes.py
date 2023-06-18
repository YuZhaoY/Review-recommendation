from flask import request
from flask_jwt_extended import create_access_token
from flasky.app.api import db
from flasky.app.api.fake import fake_bp
from flasky.app.api.fake.models import Fake
from flasky.app.api.fake.schema import FakeSchema
from flasky.app.api.utils.responses import response_with
from flasky.app.api.utils import responses as resp
from flask_jwt_extended import jwt_required


@fake_bp.route('/getFake', methods=['GET'])
def getAllRecords():
    try:
        fetched = Fake.query.all()
        fakeSchema = FakeSchema(many=True)
        fake = fakeSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"fake": fake})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)