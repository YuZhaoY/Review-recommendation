from flasky.app.api.most_fivestars import most_fivestars_bp
from flasky.app.api.most_fivestars.models import MostFivestar
from flasky.app.api.most_fivestars.schema import MostFivestarsSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@most_fivestars_bp.route('/most_fivestars', methods=['GET'])
def getAllRecords():
    try:
        fetched = MostFivestar.query.filter().all()
        mostFivestarsSchema = MostFivestarsSchema(many=True)
        mostFivestars = mostFivestarsSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"mostFivestars": mostFivestars})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)