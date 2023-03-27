from flask import Blueprint, make_response

# from app.ext.sqlalchemy import db

from .models import Coffee
# from .queries import get_all_countries_query
from .schemas import CoffeeSchema

coffees: Blueprint = Blueprint(name='coffees', import_name=__name__,)


@coffees.route('/coffees/reindex', methods=['get'])
def reindex_countries():
    Coffee.reindex()
    return make_response('Success!')


@coffees.route('/coffees/search', methods=['get'])
def full_text_search_countries():
    query, total = Coffee.search('metad plc', 1, 20)
    data = CoffeeSchema(many=True).dump(query.all())
    return f"<html><body>{data}</body></html>"
