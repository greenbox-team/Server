from flask import jsonify, request, url_for
from . import management_api
from ..models import Box
from .. import db


@management_api.route('/', methods=['POST'])
def add_box():
    box = Box.from_json(request.json)
    db.session.add(box)
    db.session.commit()
    return jsonify(box.to_json()), 201, {'Location': url_for('management_api.get_box', id=box.id)}


@management_api.route('/<int:id>')
def get_box(id):
    box = Box.query.get_or_404(id)
    return jsonify(box.to_json())
