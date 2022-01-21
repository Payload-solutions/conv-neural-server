from flask import (
    jsonify,
    request
)
import flask
from .Net.execute_model import (
    execute_model
    )
from .Net.utils import (
    performing_values,
    accuracy_loss_handler
)
from .handlers import allowed_files
import pickle
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import unittest
import os



def allowed_files(filename: str):
    ALLOWED_EXTENSIONS = {
        'png',
        'jpg'
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
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def train():
        try:
            files = request.files.get('formImageFiles')
            filename = secure_filename(files.filename)
            try:
                if not allowed_files(filename):
                    return jsonify({
                        "type": "ERROR",
                        "message": "The file type allowed should be in png or jpg"
                    })
                files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # eval_generator = process_image(filename)
                # print(test_post_image(eval_generator))
                print("ok")
                return jsonify({
                    "message": "hello"
                })
            except Exception as e:
                print(f"Error by {str(e)}")
                return jsonify({
                    "message": f"Error by {str(e)}"
                })
        except Exception as e:
            print(f"Error by {str(e)}")
            return jsonify({
                "Error": f"{str(e)}"
            })
