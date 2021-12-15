
import flask
from flask import jsonify
# from . import app


def create_error_handler(app: flask.app.Flask):

    @app.errorhandler(404)
    def not_allowed(error):
        return jsonify({
            "message": "You don't have permission to see this page",
            "error": f"{str(error)}"
        })