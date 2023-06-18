from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.user_popular.models import UserPopular
from flasky.app.api import db

class UserPopularSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserPopular
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ["user_id", "user_name", "user_fans"]
        sql_session = db.session