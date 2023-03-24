import os

import sqltap.wsgi
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from app import routes
from app.ext import elastic
from app.ext.marshmallow import ma
from app.ext.sqlalchemy import db, models  # noqa

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])

elastic.init_elasticsearch(app)

routes.register_blueprints(app)

db.init_app(app)
ma.init_app(app)

if app.debug:
    app.wsgi_app = sqltap.wsgi.SQLTapMiddleware(app.wsgi_app)
    toolbar = DebugToolbarExtension(app)

with app.app_context():
    db.create_all()
