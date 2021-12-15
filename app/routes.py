
from flask import jsonify
import flask


def create_routes(app: flask.app.Flask):

    @app.route("/hello")
    def hello():
        return jsonify(
            {"message": "Hello world"}
        )
