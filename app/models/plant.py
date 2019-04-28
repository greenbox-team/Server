from .. import db


class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date,  nullable=False)
    expected_end = db.Column(db.Date)
    end_date = db.Column(db.Date)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    species = db.relationship('Species', backref=db.backref('plants'))
    box_id = db.Column(db.Integer, db.ForeignKey('boxes.id', ondelete='CASCADE'), nullable=False)
    box = db.relationship('Box', backref=db.backref('plants'))

    def __init__(self, start_date, species_id, box_id, expected_end=None, end_date=None):
        self.start_date = start_date
        self.species_id = species_id
        self.expected_end = expected_end
        self.box_id = box_id
        self.end_date = end_date

    def __repr__(self):
        return '<Plant: {}>'.format(self.id)
