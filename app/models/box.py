from .. import db
from ..exceptions import ValidationError
from flask import current_app, request, url_for


class Box(db.Model):
    __tablename__ = 'boxes'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(45), nullable=False)

    def __init__(self, password):
        self.password = password
