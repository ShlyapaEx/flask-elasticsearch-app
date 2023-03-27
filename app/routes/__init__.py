from flask import Flask
from .countries.views import countries
from .coffee.views import coffees


BLUEPRINT_LIST = (countries, coffees)


def register_blueprints(app: Flask) -> None:
    for blueprint_name in BLUEPRINT_LIST:
        app.register_blueprint(blueprint_name)
