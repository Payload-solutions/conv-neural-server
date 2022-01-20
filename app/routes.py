from flask import (
    jsonify,
    request
)
import flask
from .Net.execute_model import execute_model
from .Net.utils import (
    performing_values,
    accuracy_loss_handler
)
import os
import pickle
from pprint import pprint
from flask_cors import cross_origin
import unittest

def create_routes(app: flask.app.Flask) -> None:

    @app.cli.command()
    def test():
        test = unittest.TestLoader().discover("tests")
        unittest.TextTestRunner().run(test)

    @app.route("/")
    def index():
        return jsonify(
            {"message": "Hello world"}
        )

    @app.route("/model")
    def train():
        """
            return the accuracy score for the neural model
        """
        # os.system("ls -la")
        print([os.popen("ls -la")])
        accuracy = execute_model()
        return jsonify({
            "accuracy": accuracy,
            "dir": ""
        })
    

    @app.route("/chart-values", methods=["GET"])
    def gallery_images():

        return jsonify({
            "message": accuracy_loss_handler()
        })

    @app.route("/about-model", methods=['GET'])
    def about_model():

        if request.method == "GET":
            # values = performing_values()
            return jsonify(performing_values())

    @app.route("/train", methods=["POST"])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def init_training():
        try:
            request.files.get('formImageFiles')
            return jsonify({
                "message": "hello"
            })
        except Exception as e:
            return jsonify({
                "Error": f"{str(e)}"
            })
