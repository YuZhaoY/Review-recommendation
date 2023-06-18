from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.review_number.models import ReviewNumber
from flasky.app.api import db

class ReviewNumberSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ReviewNumber
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ["category", "name", "rev_num", "star1", "star15", "star2", "star25", "star3", "star35", "star4", "star45", "star5"]
        sql_session = db.session