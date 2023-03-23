from flask_sqlalchemy.query import Query
from app.ext.sqlalchemy import db
from .models import Country


def add_country(name: str):
    new_country = Country(name=name)

    db.session.add(new_country)
    db.session.commit()


def get_all_countries_query() -> Query:
    return Country.query.all()
