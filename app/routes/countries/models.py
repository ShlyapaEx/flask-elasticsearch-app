from ext.sqlalchemy.models import BaseModel
from app import db


class Country(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
