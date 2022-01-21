"""This code it's for make
more readable the values of accuracy
val accuracy and so on."""
# @author: Arturo Negreiros aka (H0n3yL0xd)
from typing import (
    Dict,
    List
)
import numpy as np
import pickle
import os
from tensorflow.keras.preprocessing.image import (
    ImageDataGenerator,
    load_image,
    img_to_array
)
# from tensorflow.keras.applications.resnet50 import (
#     preprocess_input,
#     decode_predictions
# )
from typing import Any

features_type = Dict[str, float]
history_type = List[Dict[str, float]]


def performing_values() -> features_type:

    with open("lib/history_dict", "rb") as file:
        values = pickle.load(file)

    return {
        "index": 1,
        "accuracy": "{0:.2f} %".format(np.mean(values["accuracy"])*100),
        "val_accuracy": np.mean(values["val_accuracy"]),
        "loss": "{0:.2f} %".format(np.mean(values["loss"])*100),
        "val_loss": np.mean(values["val_loss"])
    }


def process_image(image):

    # img = image.load_img(f"tmp/image/{image}", 
    #     target_size=(64, 64))
    # img_array = image.img_to_array(img)
    # img_batch = np.expand_dims(img_array, axis=0)
    # img_preprocessed = preprocess_input(img_batch)
    # return img_preprocessed
    pass

def accuracy_loss_handler() -> history_type:

    with open("lib/history_dict", "rb") as file:
        values: dict = pickle.load(file)

    dataset = [
        {
            "index": i+1,
            "accuracy": a,
            "loss": b,
            "val_loss": c,
            "val_accuracy": d} for i, (a, b, c, d) in enumerate(zip(
                values["accuracy"], values["loss"], values["val_loss"], values["val_accuracy"]
            ))
    ]
    return dataset
