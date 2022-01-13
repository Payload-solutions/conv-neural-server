
from flask import jsonify
import flask
from .Net.execute_model import execute_model
import os
import pickle


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

        
    
    @app.route("/chart-values")
    def gallery_images():
        
        with open("history_dict", "rb") as file:
            values = pickle.load(file)

        return jsonify({
            "message": values
        })
    
    @app.route("/about-model")
    def about_model():
        return jsonify({
            "message": "This section gonna show the content of the model"
        })
