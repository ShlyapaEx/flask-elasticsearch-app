from app.ext.marshmallow import ma
from .models import Country


class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country
