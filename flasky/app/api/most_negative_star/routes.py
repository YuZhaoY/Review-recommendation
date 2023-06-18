from flasky.app.api.most_negative_star import most_negative_star_bp
from flasky.app.api.most_negative_star.models import MostNegative
from flasky.app.api.most_negative_star.schema import MostNegativeSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@most_negative_star_bp.route('/most_negative_star', methods=['GET'])
def getAllRecords():
    try:
        fetched = MostNegative.query.filter().all()
        mostNegativeSchema = MostNegativeSchema(many=True)
        mostNegative = mostNegativeSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"mostNegative": mostNegative})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)