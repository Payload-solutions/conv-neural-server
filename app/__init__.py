
from flask import Flask
from config import Config
import os

# local imports
from .errors import create_error_handler
from .routes import create_routes



def get_environment_config():
    if Config.FLASK_ENV == "testing":
        return "config.TestConfig"
    elif Config.FLASK_ENV == "development":
        return "config.DevelopmentConfig"
    else:
        return "config.ProductionConfig"


def create_app():

    app = Flask(__name__)

    # getting the config environment
    CONFIG_TYPE = get_environment_config()
    app.config.from_object(CONFIG_TYPE)

    # initializing routes and error handlers
    create_routes(app)
    create_error_handler(app)
    return app

