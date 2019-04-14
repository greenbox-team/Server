from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from .hardware_api import hardware_api
    app.register_blueprint(hardware_api, url_prefix='/hardware_api')

    from .management_api import management_api
    app.register_blueprint(management_api, url_prefix='/management_api')

    return app
