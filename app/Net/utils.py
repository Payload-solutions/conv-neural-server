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


features_type = Dict[str, float] 
history_type = List[Dict[str, float]]


def performing_values() -> features_type:
    
    with open("history_dict", "rb") as file:
        values = pickle.load(file)

    return {
        "index":1,
        "accuracy": "{0:.2f} %".format(np.mean(values["accuracy"])*100),
        "val_accuracy":np.mean(values["val_accuracy"]),
        "loss":"{0:.2f} %".format(np.mean(values["loss"])*100),
        "val_loss": np.mean(values["val_loss"]) 
    }


def accuracy_loss_handler() -> history_type:
    

    with open("history_dict", "rb") as file:
        values = pickle.load(file)

    
    