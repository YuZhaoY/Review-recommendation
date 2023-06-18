from flasky.app.api.most_category import most_category_bp
from flasky.app.api.most_category.models import MostCategory
from flasky.app.api.most_category.schema import MostCategorySchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@most_category_bp.route('/most_category', methods=['GET'])
def getAllRecords():
    try:
        fetched = MostCategory.query.filter().all()
        mostCategorySchema = MostCategorySchema(many=True)
        mostCategory = mostCategorySchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"mostCategory": mostCategory})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)