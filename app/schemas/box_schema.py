from .. import ma
from marshmallow import Schema, fields, post_load, validate
from ..models import Box


class BoxSchema(ma.Schema):
    id = fields.Integer()
    password = fields.String(required=True, validate=validate.Length(1))

