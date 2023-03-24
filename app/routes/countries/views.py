from flask import Blueprint, Response, make_response

from .models import Country
from .queries import get_all_countries_query
from .schemas import CountrySchema

countries: Blueprint = Blueprint(name='countries',
                                 import_name=__name__)


@countries.route('/countries', methods=['get'])
def get_all_countries():
    all_countries = get_all_countries_query()
    return CountrySchema(many=True).dump(all_countries)


@countries.route('/countries/reindex', methods=['get'])
def reindex_countries():
    Country.reindex()
    return Response('Success!')


@countries.route('/countries/search', methods=['get'])
def full_text_search_countries():
    query, total = Country.search('Russia', 1, 2)
    data = CountrySchema(many=True).dump(query.all())
    return f"<html><body>{data}</body></html>"


# @countries.route('/countries/edit', methods=['get'])
# def edit_country():
#     edited_country = Country.query.filter(Country.id == 1300).one_or_none()
#     edited_country.name = "Russia"
#     # edited_country.save()
#     return Response("OK!")
