from flask import request
from flask_jwt_extended import create_access_token
from flasky.app.api import db
from flasky.app.api.nearby_search import nearby_search_bp
from flasky.app.api.nearby_search.models import NearbySearch
from flasky.app.api.nearby_search.schema import NearbySearchSchema
from flasky.app.api.utils.responses import response_with
from flasky.app.api.utils import responses as resp
from flask_jwt_extended import jwt_required


@nearby_search_bp.route('/orderbyDistance', methods=['GET'])
def orderbyDistance():
    try:
        fetched = db.session.query(NearbySearch.business_id, NearbySearch.name, NearbySearch.address, NearbySearch.stars, NearbySearch.is_open, NearbySearch.categories, NearbySearch.distance_to_business)
        nearbySearchSchema = NearbySearchSchema(many=True)
        nearbySearch = nearbySearchSchema .dump(fetched)
        return response_with(resp.SUCCESS_200, value={"nearbySearch": nearbySearch})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

@nearby_search_bp.route('/orderbyStars', methods=['GET'])
def orderbyStars():
    try:
        fetched = db.session.query(NearbySearch.business_id, NearbySearch.name, NearbySearch.address, NearbySearch.stars, NearbySearch.is_open, NearbySearch.categories, NearbySearch.distance_to_business).order_by(NearbySearch.stars.desc())
        nearbySearchSchema = NearbySearchSchema(many=True)
        nearbySearch = nearbySearchSchema .dump(fetched)
        return response_with(resp.SUCCESS_200, value={"nearbySearch": nearbySearch})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

@nearby_search_bp.route('/isOpen', methods=['GET'])
def isOpen():
    try:
        fetched = db.session.query(NearbySearch.business_id, NearbySearch.name, NearbySearch.address, NearbySearch.stars, NearbySearch.is_open, NearbySearch.categories, NearbySearch.distance_to_business).filter(NearbySearch.is_open == 1)
        nearbySearchSchema = NearbySearchSchema(many=True)
        nearbySearch = nearbySearchSchema .dump(fetched)
        return response_with(resp.SUCCESS_200, value={"nearbySearch": nearbySearch})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)