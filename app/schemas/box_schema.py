from .. import ma
from marshmallow import fields, validate


class BoxSchema(ma.Schema):
    id = fields.Integer()
    password = fields.String(required=True, validate=validate.Length(1))

