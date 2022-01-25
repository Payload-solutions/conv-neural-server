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
    img_to_array,
    load_img
)
from typing import Any
import hashlib




features_type = Dict[str, float]
history_type = List[Dict[str, float]]


def performing_values() -> features_type:

    with open("lib/history_dict", "rb") as file:
        values = pickle.load(file)

    return {
        "index": 1,
        "accuracy": "{0:.2f}".format(np.mean(values["accuracy"])*100),
        "val_accuracy": np.mean(values["val_accuracy"]),
        "loss": "{0:.2f}".format(np.mean(values["loss"])*100),
        "val_loss": np.mean(values["val_loss"])
    }


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


# utilities
def choose_the_bigger(convolution_proves: Dict[str, float]):
    list_acc = sorted([float(convolution_proves[x])
                      for x in convolution_proves], reverse=True)
    bigger = {key: val for key, val in convolution_proves.items()
              if float(val) == list_acc[0]}
    return bigger


# hasing files
def encoding_file_name(file_name: str) -> str:
    file_name = file_name.split(".")[0]
    file_encoded = hashlib.md5(file_name.encode()).hexdigest()
    return file_encoded


def selection_image(convolution_prove: Dict[str, float],
                    temporal_file: str) -> None:
    r"""
    Basically, this function it's whenever neural training have 
    to make a decission for the image saved in the tem/image

    >>> if the accuracy is lesser or equal to the max accuracy
        and greter the loss value, then save the image in the

    :params: convolution_prove=The content whenever a test of
                image works, but we need to know if the value 
                it's secure to save in the folders for the neural
                test.

                if convolution_prove["wherever key"] <= 0.74 \
                    and convolution_prove["wherever key] > 0.68:

                    save_the_image("path_image")
                else:
                    remove_image_from_temporal_folder
    :params: temporal_file= the file saved temporaly for analyzing
    """
    bigger = choose_the_bigger(convolution_prove)
    category, value = list(bigger.keys())[0],\
        list(bigger.values())[0]
    
    if float(value) <= 0.8 and float(value) > 0.63:
        new_name = encoding_file_name(temporal_file)
        category = category.capitalize()

        img = load_img(f"temp/image/{temporal_file}")
        if category == "Low":
            img.save(
                f"app/Net/image_set/train/{category}_fat_yogurt/{category}_fat_yogurt.{new_name}.png")
        elif category == "Non":
            img.save(
                f"app/Net/image_set/train/{category}_fat_yogurt/{category}_fat_yogurt.{new_name}.png")
        else:
            img.save(
                f"app/Net/image_set/train/Regular_yogurt/Regular_yogurt.{new_name}.png")
    else:
        os.remove(f"temp/image/{temporal_file}")
