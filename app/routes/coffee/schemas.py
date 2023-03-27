from app.ext.marshmallow import ma
from .models import Coffee


class CoffeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Coffee
