# coding: utf-8
from flasky.app.api import db



class FriendRecommend(db.Model):
    __tablename__ = 'friend_recommend'
    user_id = db.Column('user_id', db.String, primary_key=True, nullable=False)
    recommend = db.Column('recommend', db.String, primary_key=True, nullable=False)


    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

