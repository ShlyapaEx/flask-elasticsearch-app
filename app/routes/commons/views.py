from flask import Blueprint, Response
from pandas_ods_reader import read_ods

files: Blueprint = Blueprint(name='files', import_name=__name__)


@files.route('/files/import_data', methods=['get'])
def import_data():
    return Response("123")
