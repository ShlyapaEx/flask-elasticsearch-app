from ssl import create_default_context

from elasticsearch import Elasticsearch
from flask import Flask


def init_elasticsearch(app: Flask):
    if app.config['ELASTICSEARCH_URL']:
        context = create_default_context(cafile=app.config['PATH_TO_CA_CERT'])
        app.elasticsearch = Elasticsearch(hosts=app.config['ELASTICSEARCH_URL'],
                                          http_auth=(app.config['ELASTICSEARCH_LOGIN'],
                                                     app.config['ELASTICSEARCH_PASSWORD']),                                  # make sure we verify SSL certificates
                                          verify_certs=True,
                                          ssl_context=context)
        try:
            app.elasticsearch.info()
        except ConnectionError as err:
            print(err)
            raise ConnectionError from err
    else:
        app.elasticsearch = None
