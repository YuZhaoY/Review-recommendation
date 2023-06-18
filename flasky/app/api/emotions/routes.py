from flask import request
from flask_jwt_extended import create_access_token
from flasky.app.api import db
from flasky.app.api.emotions import emotions_bp
from flasky.app.api.emotions.models import Emotions
from flasky.app.api.emotions.schema import EmotionsSchema
from flasky.app.api.utils.responses import response_with
from flasky.app.api.utils import responses as resp
from flask_jwt_extended import jwt_required


@emotions_bp.route('/getEmotions', methods=['GET'])
def getRecords():
    try:
        fetched = Emotions.query.all()
        emotionsSchema = EmotionsSchema(many=True)
        emotions = emotionsSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"emotions": emotions})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

