from app.ext.sqlalchemy import db
from app.ext.elastic.models import SearchableMixin
# from app.ext.sqlalchemy.models import BaseModel


class Country(SearchableMixin, db.Model):
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country = db.Column(db.ForeignKey('country.id'))
