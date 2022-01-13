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


history_type = Dict[str, float]


def performing_values() -> history_type:
    
    with open("history_dict", "rb") as file:
        values = pickle.load(file)

    return {
        "accuracy": np.mean(values["accuracy"]),
        "val_accuracy":np.mean(values["val_accuracy"]),
        "loss":np.mean(values["loss"]),
        "val_loss": np.mean(values["val_loss"]) 
    }

