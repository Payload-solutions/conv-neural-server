
from flask import jsonify
from . import app


@app.route("/hello")
def hello():
    return jsonify(
        {"message": "Hello world"}
    )
