from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.userrecs.models import Userrecs
from flasky.app.api import db

class UserrecsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Userrecs
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ['f1','user','recommendations','rev_user_id','rev_business_id','rev_stars','business']
        sql_session = db.session