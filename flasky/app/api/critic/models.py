# coding: utf-8
from flasky.app.api import db



class Critic(db.Model):
    __tablename__ = 'critic'
    user_id = db.Column('user_id', db.String, primary_key=True, nullable=False)
    user_name = db.Column('user_name', db.String)
    user_review_count = db.Column('user_review_count', db.Integer)

    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

