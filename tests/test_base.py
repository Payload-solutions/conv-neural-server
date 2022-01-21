from flask_testing import TestCase
from wsgi import app
from flask import (
    current_app,
    url_for
)
from io import StringIO
from PIL import Image

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
    
    def test_hsitory_values_get(self):
        response = self.client.get(url_for("history_values"))
        self.assert200(response)
    
    def test_about_model_get(self):
        response = self.client.get(url_for("about_model"))
        self.assert200(response)
    
    def test_train_post(self):
        image = Image.open("temp/image/hola.png")
        response = self.client.post(url_for("train"), 
            data={
                "formImageFiles": (image, 'hola.png')
            })
        
        self.assertEquals(response.status, "200 OK")

