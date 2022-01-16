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

    return model.evaluate(test_generator)[1]


def test_post_image():
    pass