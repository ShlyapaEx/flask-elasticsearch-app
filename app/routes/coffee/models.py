from ext.sqlalchemy.models import BaseModel
from app import db


class Coffee(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String)
    country_of_origin_id = db.Column(db.String, db.ForeignKey('Country'))
    number_of_bags = db.Column()
