# coding: utf-8
from flasky.app.api import db



class WordCount(db.Model):
    __tablename__ = 'word_count'
    name = db.Column('word', db.String, primary_key=True, nullable=False)
    value = db.Column('counts', db.Integer)



    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

