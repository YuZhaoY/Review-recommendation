from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.city_best_business.models import CityBestBusiness
from flasky.app.api import db

class CityBestBusinessSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CityBestBusiness
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ["business_id", "name", "city", "stars"]
        sql_session = db.session