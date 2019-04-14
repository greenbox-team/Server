from flask import Blueprint

hardware_api = Blueprint('hardware_api', __name__)

from . import boxes
