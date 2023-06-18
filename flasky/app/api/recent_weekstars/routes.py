from datetime import datetime, timedelta

from flasky.app.api.recent_weekstars import recent_weekstars_bp
from flasky.app.api.recent_weekstars.models import RecentWeedstars
from flasky.app.api.recent_weekstars.schema import RecentWeedstarsSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@recent_weekstars_bp.route('/recent_weekstars', methods=['POST'])
def getAllRecords():
    try:
        data = request.get_json()
        print(data)
        value = data['date']
        print(value)
        date1 = datetime.strptime(value, "%Y-%m-%d")
        fetched = RecentWeedstars.query.filter(RecentWeedstars.rev_date> date1-timedelta(7), RecentWeedstars.rev_date <= date1).all()
        recentWeedstarsSchema = RecentWeedstarsSchema(many=True)
        recentWeedstars = recentWeedstarsSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"recentWeedstars": recentWeedstars})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)