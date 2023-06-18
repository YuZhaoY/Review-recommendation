# coding: utf-8
from flasky.app.api import db



class Userrecs(db.Model):
    __tablename__ = 'userrecs'
    f1 = db.Column('f1', db.String, primary_key=True, nullable=False)
    user = db.Column('user', db.String)
    recommendations = db.Column('recommendations', db.String)
    rev_user_id = db.Column('rev_user_id', db.String)
    rev_business_id = db.Column('rev_business_id', db.String)
    rev_stars = db.Column('rev_stars', db.String)
    business = db.Column('business', db.String)

    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

