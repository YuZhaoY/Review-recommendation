from flasky.app.api.best_category import best_category_bp
from flasky.app.api.best_category.models import BestCategory
from flasky.app.api.best_category.schema import BestCategorySchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@best_category_bp.route('/best_category', methods=['POST'])
def getAllRecords():
    try:
        data = request.get_json()
        value=data['category']
        print(value)
        fetched = BestCategory.query.filter(BestCategory.category == value).all()
        bestCategorySchema = BestCategorySchema(many=True)
        bestCategory = bestCategorySchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"bestCategory": bestCategory})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)