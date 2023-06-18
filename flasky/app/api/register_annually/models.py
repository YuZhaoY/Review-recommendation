# coding: utf-8
from flasky.app.api import db



class RegisterAnnually(db.Model):
    __tablename__ = 'register_annually'
    year = db.Column('year', db.Integer, primary_key=True, nullable=False)
    count = db.Column('count(1)', db.BigInteger, nullable=False)

    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

