from flasky.app.api.word_count import word_count_bp
from flasky.app.api.word_count.models import WordCount
from flasky.app.api.word_count.schema import WordCountSchema
from flasky.app.api.utils import responses as resp
from flasky.app.api.utils.responses import response_with
from flask import request

@word_count_bp.route('/word_count', methods=['GET'])
def getAllRecords():
    try:
        fetched = WordCount.query.filter().all()
        wordCountSchema = WordCountSchema(many=True)
        wordCount = wordCountSchema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"wordCount": wordCount})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)