from flasky.app.api.Business_Referrals import business_referrals_bp
from flasky.app.api.Business_Referrals.models import BusinessReferrals
from flasky.app.api.Business_Referrals.schema import BusinessReferralsSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@business_referrals_bp.route('/business_referrals', methods=['GET'])
def getAllRecords():
    try:
        fetched = BusinessReferrals.query.all()
        businessReferralsSchema = BusinessReferralsSchema(many=True)
        businessReferrals = businessReferralsSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"businessReferrals": businessReferrals})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)