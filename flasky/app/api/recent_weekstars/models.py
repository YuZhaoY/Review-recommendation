# coding: utf-8
from flasky.app.api import db



class RecentWeedstars(db.Model):
    __tablename__ = 'recent_weekstars'
    rev_business_id = db.Column('rev_business_id', db.String, primary_key=True, nullable=False)
    rev_date = db.Column('rev_date', db.Date)
    rev_stars = db.Column('rev_stars', db.Integer)



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

