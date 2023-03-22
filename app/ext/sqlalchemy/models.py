from sqlalchemy.ext.declarative import declarative_base, declared_attr

from app.utils.string_operations import camel_to_snake
from app import db


class _BaseModel(db.Model):

    @declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__).replace('_model', '')


BaseModel = declarative_base(cls=_BaseModel)
