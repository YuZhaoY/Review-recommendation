from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.Business_Referrals.models import BusinessReferrals
from flasky.app.api import db

class BusinessReferralsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BusinessReferrals
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ["Business_Referrals"]
        sql_session = db.session