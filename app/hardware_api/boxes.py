from flask import jsonify
from . import hardware_api


@hardware_api.route('/', methods=['GET'])
def get_state():
    """
        Testing
    """
    test = {
        "box": 1
    }

    return jsonify(test)

