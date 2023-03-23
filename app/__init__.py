import os

from flask import Flask

from app import routes
from app.ext.sqlalchemy import db, models
from app.ext.marshmallow import ma
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])

routes.register_blueprints(app)

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()
