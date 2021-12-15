
from flask import Flask
from config import Config
import os

# local imports
from .errors import create_error_handler
from .routes import create_routes



# def get_environment_config():
#     if Config.ENV == "TESTING":
#         return "config.TestConfig"
#     elif Config.ENV == "DEVELOPMENT":
#         return "config.DevelopmentConfig"
#     else:
#         return "config.ProductionConfig"


def create_app():

    app = Flask(__name__)

    # getting the config environment
    CONFIG_TYPE = os.getenv("CONFIG_TYPE", default='config.DevelopmentConfig')
    print(CONFIG_TYPE)
    app.config.from_object(CONFIG_TYPE)
    create_routes(app)
    create_error_handler(app)
    return app
    # pprint(os.environ)
