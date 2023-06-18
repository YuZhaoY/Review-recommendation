# coding: utf-8
from flasky.app.api import db



class MostCategory(db.Model):
    __tablename__ = 'most_category'
    name = db.Column('name', db.String, primary_key=True, nullable=False)
    value = db.Column('category_count', db.Integer)



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

