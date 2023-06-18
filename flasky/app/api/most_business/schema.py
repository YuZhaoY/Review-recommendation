from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.most_business.models import MostBusiness
from flasky.app.api import db

class MostBusinessSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MostBusiness
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ["name", "name_count", "avg_stars"]
        sql_session = db.session