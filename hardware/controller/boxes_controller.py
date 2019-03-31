from flask import Blueprint, request, jsonify
from dal.repository import box_repository

boxes_controller = Blueprint('boxes_controller', __name__)


@boxes_controller.route('/', methods=['POST'])
def synchronize_sensors():
    """
        Testing
    """
    content = request.get_json()

    box_repository.add(content)
    test = {
        "box": 1
    }

    return jsonify(test)
