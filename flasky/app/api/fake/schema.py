from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.fake.models import Fake
from flasky.app.api import db

class FakeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Fake
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ['index','restaurantID','reviewerID','rating','reviewUsefulCount','reviewContent','date','reviewCount','usefulCount','coolCount','funnyCount','complimentCount','restaurantRating','fanCount','predict']
        sql_session = db.session