from flask import Blueprint

management_api = Blueprint('management_api', __name__)

from . import boxes
from . import climate
