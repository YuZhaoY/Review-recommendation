from flasky.app.api.review_number import review_number_bp
from flasky.app.api.review_number.models import ReviewNumber
from flasky.app.api.review_number.schema import ReviewNumberSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@review_number_bp.route('/review_number', methods=['POST'])
def getAllRecords():
    try:
        data = request.get_json()
        value = data['category']
        print(value)
        fetched = ReviewNumber.query.filter(ReviewNumber.category == value).all()
        reviewNumberSchema = ReviewNumberSchema(many=True)
        reviewNumber = reviewNumberSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"reviewNumber": reviewNumber})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)