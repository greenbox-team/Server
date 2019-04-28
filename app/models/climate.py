from .. import db


class Climate(db.Model):
    __tablename__ = 'climate'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    temperature = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    light = db.Column(db.Integer, nullable=False)
    soil_humidity = db.Column(db.Integer)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id', ondelete='CASCADE'), nullable=False)
    plant = db.relationship('Plant', backref=db.backref('climate'))

    def __init__(self, start_date, end_date, temperature, light, humidity, soil_humidity=None):
        self.start_date = start_date
        self.end_date = end_date
        self.temperature = temperature
        self.light = light
        self.humidity = humidity
        self.soil_humidity = soil_humidity
