# coding: utf-8
from flasky.app.api import db



class BestCategory(db.Model):
    __tablename__ = 'categories_stars'
    business_id = db.Column('business_id', db.String, primary_key=True, nullable=False)
    avg_stars = db.Column('avg_stars', db.Float, primary_key=True, nullable=False)
    category = db.Column('category', db.String)


    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

