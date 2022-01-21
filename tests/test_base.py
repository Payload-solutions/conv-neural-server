from flask_testing import TestCase
from wsgi import app
from flask import (
    current_app,
    url_for
)


class MainTest(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config["TESTING"])
    
    # def test_train_get(self):
    #     response = self.client.get(url_for("train"))
    #     self.assert200(response)
    
    def test_hsitory_values_get(self):
        response = self.client.get(url_for("history_values"))
        self.assert200(response)
    
    def test_about_model_get(self):
        response = self.client.get(url_for("about_model"))
        self.assert200(response)
