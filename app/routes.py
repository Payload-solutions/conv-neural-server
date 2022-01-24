from flask import (
    jsonify,
    request
)
import flask
from .Net.execute_model import (
    execute_model,
    test_post_image
)
from .Net.utils import (
    performing_values,
    accuracy_loss_handler
)
from .handler_messages import response_conv_handler
from .handlers import allowed_files
import pickle
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import unittest
import os


def allowed_files(filename: str):
    ALLOWED_EXTENSIONS = {
        'png',
        'jpg',
        'jpeg'
    }
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower()\
        in ALLOWED_EXTENSIONS


def create_routes(app: flask.app.Flask) -> None:

    @app.cli.command()
    def test():
        test = unittest.TestLoader().discover("tests")
        unittest.TextTestRunner().run(test)

    @app.route("/history_values", methods=["GET"])
    def history_values():
        return jsonify({
            "message": accuracy_loss_handler()
        })

    @app.route("/about_model", methods=["GET"])
    def about_model():
        """
        Getting all the values saved making the neural
        training and saving in json files
        """
        return jsonify(performing_values())

    @app.route("/train", methods=["POST"])
    @cross_origin(origin='localhost', headers=['Content- Type',
        'Authorization'])
    def train():
        try:
            files = request.files.get('formImageFiles')
            filename = secure_filename(files.filename)

            try:
                if not allowed_files(filename):
                    return jsonify(response_conv_handler(
                        message="Error trying to receive the image",
                        type="ERROR"))

                files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                content = test_post_image(f"temp/image/{filename}")
                
                print(content)
                # return jsonify({"prediction":content})
                return jsonify(response_conv_handler(content=content))
            except Exception as e:
                return jsonify(response_conv_handler(
                    message="Error trying to parse the image",
                    type="ERROR"))
        except Exception as e:
            return jsonify(response_conv_handler(
                message="Error trying to receive the image",
                type="ERROR"))



