
import flask
from flask import jsonify


def create_error_handler(app: flask.app.Flask) -> None:

    @app.errorhandler(400)
    def bad_requests(error):
        return jsonify({
            "message": "Bad requests performed",
            "code": 400
        })
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "message": "You don't have permission to see this content",
            "code": 401
        })
    
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "message": "Forbidden site",
            "code": 403
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "message": "The content you are looking for doesn't exists",
            "code": 404
        })
    
    