from flask import Blueprint
from .queries import get_all_countries_query
from .schemas import CountrySchema

countries: Blueprint = Blueprint(name='countries',
                                 import_name=__name__)


@countries.route('/countries', methods=['get'])
def get_all_countries():
    all_countries = get_all_countries_query()
    return CountrySchema(many=True).dump(all_countries)
