import os
import click


class Config:
    ENV = os.environ["ENV"] if "ENV" in os.environ else "DEVELOPMENT"
    CSRF_ENABLED = True
    SECRET_KEY = "this is the secret key"

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig():
    DEBUG=False