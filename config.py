import os

class Config:
    FLASK_ENV = os.environ["FLASK_ENV"]
    DEBUG=False
    TESTING=False
    CSRF_ENABLED = True
    SECRET_KEY = "this is the secret key"

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    FLASK_ENV=os.environ["FLASK_ENV"]
    TESTING=True
    DEBUG=False

class ProductionConfig(Config):
    FLASK_ENV = os.environ["FLASK_ENV"]
    DEBUG=False