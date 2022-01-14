
import flask
from flask import Flask
from config import Config
import os
from flask_cors import CORS
# local imports
from .errors import create_error_handler
from .routes import create_routes


# custom variables
flask_app = flask.app.Flask


def get_environment_config():
    if Config.FLASK_ENV == "testing":
        return "config.TestConfig"
    elif Config.FLASK_ENV == "production":
        return "config.ProductionConfig"
    else:
        return "config.DevelopmentConfig"


def create_app() -> flask_app:

    app = Flask(__name__)

    CORS(app, resources={r'/*': {'origins':'*'}})
    # getting the config environment
    CONFIG_TYPE = get_environment_config()
    app.config.from_object(CONFIG_TYPE)

    # initializing routes and error handlers
    create_routes(app)
    create_error_handler(app)
    return app

