from flask import Blueprint, request, jsonify

boxes_controller = Blueprint('boxes_controller', __name__)


@boxes_controller.route('/', methods=['GET'])
def synchronize_sensors():
    """
        Testing
    """
    test = {
        "box": 1
    }

    return jsonify(test)
