from .Net import Net
from pprint import pprint
import pickle


def execute_model():

    net = Net(
        train_path="app/Net/image_set/train", 
        test_path="app/Net/image_set/test", 
        valid_path="app/Net/image_set/validator"
        )
    
    train_generator, test_generator, valid_generator = net.load_image_set()
    model = net.neural_model(train_generator, valid_generator)
    pprint(model.history)

    # dict_path = "history_dict"

    # with open(dict_path, "rb") as file:
    #    elements = pickle.load(file)

    # pprint(elements)
    return model.evaluate(test_generator)[1]
