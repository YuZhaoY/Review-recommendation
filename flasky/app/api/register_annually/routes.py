from flasky.app.api.register_annually import register_annually_bp
from flasky.app.api.register_annually.models import RegisterAnnually
from flasky.app.api.register_annually.schema import RegisterAnnuallySchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with


@register_annually_bp.route('/getRegisterAnnually', methods=['GET'])
def getAllRecords():
    try:
        fetched = RegisterAnnually.query.all()
        registerAnnuallySchema = RegisterAnnuallySchema(many=True)
        registerAnnually = registerAnnuallySchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"registerAnnually": registerAnnually})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)