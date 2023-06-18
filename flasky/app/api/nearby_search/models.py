# coding: utf-8
from flasky.app.api import db



class NearbySearch(db.Model):
    __tablename__ = 'nearby_search'
    business_id = db.Column('business_id', db.String, primary_key=True, nullable=False)
    name = db.Column('name', db.String)
    address = db.Column('address', db.String)
    city = db.Column('city', db.String)
    state = db.Column('state', db.String)
    postal_code = db.Column('postal_code', db.String)
    latitude = db.Column('latitude', db.Float)
    longitude = db.Column('longitude', db.Float)
    stars = db.Column('stars', db.Float)
    review_count = db.Column('review_count', db.Integer)
    is_open = db.Column('is_open', db.Integer)
    attributes = db.Column('attributes', db.String)
    categories = db.Column('categories', db.String)
    hours = db.Column('hours', db.String)
    distance_to_business = db.Column('distance_to_business', db.Float)

    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

