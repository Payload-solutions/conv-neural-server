import os

class Config:
    FLASK_ENV = "development"
    DEBUG=False
    TESTING=False
    CSRF_ENABLED = True
    SECRET_KEY = "this is the secret key"

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    TESTING=True
    DEBUG=False

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG=False