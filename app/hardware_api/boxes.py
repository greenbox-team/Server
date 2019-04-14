from flask import jsonify
from . import hardware_api


@hardware_api.route('/users/', methods=['GET'])
def synchronize_sensors():
    """
        Testing
    """
    test = {
        "box": 1
    }

    return jsonify(test)

