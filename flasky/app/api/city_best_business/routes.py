from flasky.app.api.city_best_business import city_best_business_bp
from flasky.app.api.city_best_business.models import CityBestBusiness
from flasky.app.api.city_best_business.schema import CityBestBusinessSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@city_best_business_bp.route('/city_best_business', methods=['POST'])
def getAllRecords():
    try:
        data = request.get_json()
        print(data)
        value = data['city']
        print(value)
        fetched = CityBestBusiness.query.filter(CityBestBusiness.city == value).all()
        cityBestBusinessSchema = CityBestBusinessSchema(many=True)
        cityBestBusiness = cityBestBusinessSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"cityBestBusiness": cityBestBusiness})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)