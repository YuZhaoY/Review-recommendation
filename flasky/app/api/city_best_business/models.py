# coding: utf-8
from flasky.app.api import db



class CityBestBusiness(db.Model):
    __tablename__ = 'city_best_business'
    business_id = db.Column('business_id', db.String, primary_key=True, nullable=False)
    name = db.Column('name', db.String)
    city = db.Column('city', db.String)
    stars = db.Column('stars', db.Float)



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

