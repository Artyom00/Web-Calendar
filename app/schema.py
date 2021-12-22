from marshmallow import fields
from . import ma
from .models import Events


# Creating a JSON schema based on Events model
class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Events
        load_instance = True  # Deserialization to Events object
