from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flasky.app.api.nearby_search.models import NearbySearch
from flasky.app.api import db

class NearbySearchSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = NearbySearch
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
        include_fk = True  # 序序列阶段是否也一并返回主键
        load_instance = True  # 反序列化阶段时，直接返回模型对象
        fields = ['business_id','name','address','city','state','postal_code','latitude','longitude','stars','review_count','is_open','attributes','categories','hours','distance_to_business']
        sql_session = db.session