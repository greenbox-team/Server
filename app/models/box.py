from .. import db


class Box(db.Model):
    __tablename__ = 'boxes'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(30), nullable=False)

    def __init__(self, password):
        self.password = password

    def __repr__(self):
        return '<Box {}>'.format(self.id)
