from .. import db
from ..exceptions import ValidationError
from flask import current_app, request, url_for



class Climate(db.Model):
    __tablename__ = 'climate'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    light = db.Column(db.Integer)
    soil_humidity = db.Column(db.Integer)
    password = db.Column(db.String(45))
