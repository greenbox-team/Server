from flask import Flask
from app.controller.boxes_controller import boxes_controller

app = Flask(__name__)
app.register_blueprint(boxes_controller)
