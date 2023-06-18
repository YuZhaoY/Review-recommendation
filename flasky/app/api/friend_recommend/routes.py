from flasky.app.api.friend_recommend import friend_recommend_bp
from flasky.app.api.friend_recommend.models import FriendRecommend
from flasky.app.api.friend_recommend.schema import FriendRecommendSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@friend_recommend_bp.route('/friend_recommend', methods=['GET'])
def getAllRecords():
    try:
        fetched = FriendRecommend.query.all()
        friendRecommendSchema = FriendRecommendSchema(many=True)
        friendRecommend = friendRecommendSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"friendRecommend": friendRecommend})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)