from flask import request
from flask_jwt_extended import create_access_token
from flasky.app.api import db
from flasky.app.api.critic import critic_bp
from flasky.app.api.critic.models import Critic
from flasky.app.api.critic.schema import CriticSchema
from flasky.app.api.utils.responses import response_with
from flasky.app.api.utils import responses as resp
from flask_jwt_extended import jwt_required


@critic_bp.route('/getCritic', methods=['GET'])
def getAllRecords():
    try:
        fetched = Critic.query.all()
        criticSchema = CriticSchema(many=True)
        critic = criticSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"registerAnnually": critic})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)