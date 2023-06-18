# coding: utf-8
from flasky.app.api import db



class Emotions(db.Model):
    __tablename__ = 'emotions'
    index = db.Column('index', db.BIGINT, primary_key=True, nullable=False)
    rev_text = db.Column('rev_text', db.String)
    rev_stars = db.Column('rev_stars', db.BIGINT)
    ID = db.Column('ID', db.BIGINT)
    rev_class = db.Column('rev_class', db.BIGINT)
    predict = db.Column('predict', db.BIGINT)
    predict_class = db.Column('predict_class', db.String(255))



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

