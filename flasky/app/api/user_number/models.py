# coding: utf-8
from flasky.app.api import db



class UserNumber(db.Model):
    __tablename__ = 'user_number'
    year = db.Column('year', db.String, primary_key=True, nullable=False)
    user_number = db.Column('user_number', db.Integer)
    elite_number = db.Column('elite_number', db.Integer)
    silence_number = db.Column('silence_number', db.Integer)
    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

