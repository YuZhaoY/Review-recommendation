# coding: utf-8
from flasky.app.api import db



class MostNegative(db.Model):
    __tablename__ = 'most_negative_star'
    name = db.Column('name', db.String, primary_key=True, nullable=False)
    negative_num = db.Column('negative_num', db.Integer)



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

