
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



def create_routes(app: flask.app.Flask) -> None:

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
            "dir":""         
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
    def init_training():
        if request.method == "POST":
            print(dir(request))





