from sqlalchemy_utils import ChoiceType

from app.ext.elastic.models import SearchableMixin
from app.ext.sqlalchemy import db


class Coffee(SearchableMixin, db.Model):
    __searchable__ = ['owner', 'number_of_bags', 'grading_date',
                      'aroma', 'certification_body']

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String)
    owner = db.Column(db.String)
    country_of_origin = db.Column(db.ForeignKey('country.id',
                                                ondelete='SET NULL'))
    region = db.Column(db.ForeignKey('region.id', ondelete='SET NULL'))
    number_of_bags = db.Column(db.Integer)
    grading_date = db.Column(db.DateTime)
    processing_method = db.Column(db.String)
    aroma = db.Column(db.Float)
    flavor = db.Column(db.Float)
    sweetness = db.Column(db.Float)
    total_cup_points = db.Column(db.Float)
    certification_body = db.Column(db.String)
