# coding: utf-8
from flasky.app.api import db



class Fake(db.Model):
    __tablename__ = 'fake'
    index = db.Column('index', db.BIGINT, primary_key=True, nullable=False)
    restaurantID = db.Column('restaurantID', db.String)
    reviewerID = db.Column('reviewerID', db.String)
    rating = db.Column('rating', db.BIGINT)
    reviewUsefulCount = db.Column('reviewUsefulCount', db.BIGINT)
    reviewContent = db.Column('reviewContent', db.String)
    date = db.Column('date', db.String)
    reviewCount = db.Column('reviewCount', db.BIGINT)
    usefulCount = db.Column('usefulCount', db.BIGINT)
    coolCount = db.Column('coolCount', db.BIGINT)
    funnyCount = db.Column('funnyCount', db.BIGINT)
    complimentCount = db.Column('complimentCount', db.BIGINT)
    restaurantRating = db.Column('restaurantRating', db.Float)
    fanCount = db.Column('fanCount', db.BIGINT)
    predict = db.Column('predict', db.String)

    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

