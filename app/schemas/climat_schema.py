from .. import ma
from marshmallow import fields, validate


class ClimateSchema(ma.Schema):
    id = fields.Integer()
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    temperature = fields.Integer(required=True)
    humidity = fields.Integer(required=True)
    light = fields.Integer(required=True)
    soil_humidity = fields.Integer()
    plant_id = fields.Integer(required=True)
