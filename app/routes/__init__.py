from flask import Flask
from .countries.views import countries
from .commons.views import files


BLUEPRINT_LIST = (countries, files)


def register_blueprints(app: Flask) -> None:
    for blueprint_name in BLUEPRINT_LIST:
        app.register_blueprint(blueprint_name)
