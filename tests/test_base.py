from flask_testing import TestCase
from wsgi import app
from flask import current_app


class MainTest(TestCase):
    
    def create_app(self):
        # app = create_app()
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)