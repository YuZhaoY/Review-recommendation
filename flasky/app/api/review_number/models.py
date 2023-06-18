# coding: utf-8
from flasky.app.api import db

class ReviewNumber(db.Model):
    __tablename__ = 'review_number'
    category = db.Column('category', db.String, primary_key=True, nullable=False)
    name = db.Column('name', db.String, primary_key=True, nullable=False)
    rev_num = db.Column('review_num', db.BIGINT)
    star1 = db.Column('1', db.BIGINT)
    star15 = db.Column('1.5', db.BIGINT)
    star2 = db.Column('2', db.BIGINT)
    star25 = db.Column('2.5', db.BIGINT)
    star3 = db.Column('3', db.BIGINT)
    star35 = db.Column('3.5', db.BIGINT)
    star4 = db.Column('4', db.BIGINT)
    star45 = db.Column('4.5', db.BIGINT)
    star5 = db.Column('5', db.BIGINT)


    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

