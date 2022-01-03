
from flask import jsonify
import flask
from Net.execute_model import execute_model


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

        accuracy = execute_model()
        return jsonify({
            "accuracy": accuracy
        })
    
    @app.route("/gallery")
    def gallery_images():
        return jsonify({
            "message": "This is the route images"
        })
    
    @app.route("/about-model")
    def about_model():
        return jsonify({
            "message": "This section gonna show the content of the model"
        })
