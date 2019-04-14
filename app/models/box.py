from .. import db
from ..exceptions import ValidationError
from flask import current_app, request, url_for



class Box(db.Model):
    __tablename__ = 'boxes'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(45))

    @staticmethod
    def from_json(json_box):
        print(json_box)
        password = json_box.get('password')
        if password is None or password == '':
            raise ValidationError('post does not have a body')
        return Box(password=password)

    def to_json(self):
        json_box = {
            'url': url_for('management_api.get_box', id=self.id),
            'password': self.password
        }
        return json_box
