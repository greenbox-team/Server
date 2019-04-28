from flask import jsonify, request, url_for
from . import management_api
from ..models import Climate
from marshmallow import ValidationError
from ..schemas import ClimateSchema
from .. import db

climate_schema = ClimateSchema()
climates_schema = ClimateSchema(many=True)


@management_api.route('/climate', methods=['POST'])
def add_climate():
    json_data = request.get_json(force=True)
    if not json_data:
        return 400

    try:
        data = climate_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    climate = Climate(
        data['start_date'],
        data['end_date'],
        data['temperature'],
        data['light'],
        data['humidity'],
        data['soil_humidity']
    )

    db.session.add(climate)
    db.session.commit()
    result = climate_schema.dump(climate)

    return jsonify(result), 201


@management_api.route('/climate/<int:plant_id>')
def get_climate(plant_id):
    climate = Climate.query(Climate.plant_id).get_or_404(plant_id)
    climate = climates_schema.dump(climate)
    return jsonify(climate), 200
