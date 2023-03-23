from app.ext.sqlalchemy import db
# from app.ext.sqlalchemy.models import BaseModel


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country = db.Column(db.ForeignKey('country.id'))
