from flask import Flask
from hardware.controller.boxes_controller import boxes_controller

hardware = Flask(__name__)
hardware.register_blueprint(boxes_controller)
