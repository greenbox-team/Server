from flask import jsonify, request, url_for
from . import management_api
from ..models import Box
from marshmallow import ValidationError
from ..schemas import BoxSchema
from .. import db

box_schema = BoxSchema()
boxes_schema = BoxSchema(many=True)


@management_api.route('/boxes', methods=['POST'])
def add_box():
    json_data = request.get_json(force=True)
    if not json_data:
        return 400

    try:
        data = box_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    box = Box(
        data['password']
    )

    db.session.add(box)
    db.session.commit()
    result = box_schema.dump(box)

    return jsonify(result), 201


@management_api.route('/boxes/<int:id>')
def get_box(id):
    box = Box.query.get_or_404(id)
    box = box_schema.dump(box)
    return jsonify(box), 200


@management_api.route('/boxes')
def get():
    boxes = Box.query.all()
    boxes = boxes_schema.dump(boxes)
    return jsonify(boxes), 200
