from flasky.app.api.most_business import most_business_bp
from flasky.app.api.most_business.models import MostBusiness
from flasky.app.api.most_business.schema import MostBusinessSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@most_business_bp.route('/most_business', methods=['GET'])
def getAllRecords():
    try:
        fetched = MostBusiness.query.filter().all()
        mostBusinessSchema = MostBusinessSchema(many=True)
        mostBestBusiness = mostBusinessSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"mostBestBusiness": mostBestBusiness})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)