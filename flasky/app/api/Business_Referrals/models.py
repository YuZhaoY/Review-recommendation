# coding: utf-8
from flasky.app.api import db



class BusinessReferrals(db.Model):
    __tablename__ = 'business_referrals'
    Business_Referrals = db.Column('Business_Referrals', db.String, primary_key=True, nullable=False)


    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

