# coding: utf-8
from flasky.app.api import db



class MostFivestar(db.Model):
    __tablename__ = 'most_fivestar'
    name = db.Column('name', db.String, primary_key=True, nullable=False)
    fivestar_num = db.Column('fivestar_num', db.Integer)



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

