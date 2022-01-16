#!/usr/bin/python3


import pickle
from pprint import pprint


def handling():

    with open("history_dict", "rb") as file:
        values: dict = pickle.load(file)
    
    # dataset = [
    #     {"accuracy": "", 
    #     "val_accuracy":"", 
    #     "loss":"", 
    #     "val_loss":""} for  ]

    for key, val in values.items():
        for i, x in enumerate(val):
            print(key, i, x)
            
            
            if i == 2:
                break

handling()