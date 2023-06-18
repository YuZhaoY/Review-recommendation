from flasky.app.api.categories_numbers import categories_number_bp
from flasky.app.api.categories_numbers.models import CategoriesNumber
from flasky.app.api.categories_numbers.schema import CategoriesNumberSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with


@categories_number_bp.route('/categories_number', methods=['GET'])
def getAllRecords():
    try:
        fetched = CategoriesNumber.query.all()
        categoriesNumberSchema = CategoriesNumberSchema(many=True)
        categoriesNumber = categoriesNumberSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"categoriesNumber": categoriesNumber})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)