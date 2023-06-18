# coding: utf-8
from flasky.app.api import db



class CategoriesNumber(db.Model):
    __tablename__ = 'categories_number'
    category = db.Column('category', db.String, primary_key=True, nullable=False)
    categories_number = db.Column('categories_number', db.BigInteger, nullable=False)

    # @classmethod
    # def find_all_record(cls):
    #     return cls.query(RegisterAnnually.year, RegisterAnnually.count)

