#!/usr/bin/python3


import pickle
from pprint import pprint


def handling():

    with open("history_dict", "rb") as file:
        values: dict = pickle.load(file)
    
    dataset = [
        {
            "index":i+1,
            "accuracy": b, 
            "val_accuracy":d, 
            "loss": a, 
            "val_loss":c} for i, (a, b, c, d) in enumerate(zip(
                values["loss"],
                values["accuracy"],
                values["val_loss"],
                values["val_accuracy"]
        ))
    ]

    pprint(dataset)

handling()