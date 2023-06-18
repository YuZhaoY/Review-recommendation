# coding: utf-8
from flasky.app.api import db



class MostBusiness(db.Model):
    __tablename__ = 'most_business'
    name = db.Column('name', db.String, primary_key=True, nullable=False)
    name_count = db.Column('name_count', db.Integer)
    avg_stars = db.Column('avg_stars', db.Float)



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

