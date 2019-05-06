from flask import jsonify
from datetime import datetime
from sqlalchemy import and_
from ..models import Climate, Plant
from ..schemas import ClimateSchema
from . import hardware_api

climate_schema = ClimateSchema()


@hardware_api.route('/boxes/<int:box_id>', methods=['GET'])
def get_climate(box_id):
    plant = Plant.query.filter(
        and_(
            Plant.box_id == box_id,
            Plant.end_date.is_(None)
        )
    ).first()
    if not plant:
        return jsonify({'message': 'not found'}), 404

    climate = Climate.query.filter(
        and_(
            Climate.plant_id == plant.id,
            Climate.start_date <= datetime.now(),
            Climate.end_date >= datetime.now()
        )
    ).first()
    climate = climate_schema.dump(climate)
    return jsonify(climate)

