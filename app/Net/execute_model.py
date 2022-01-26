# the core of the architecture
from .Net import Net
import pickle

from tensorflow.keras.preprocessing.image import (
    array_to_img,
    img_to_array,
    load_img,
    ImageDataGenerator
)
from PIL import Image
from typing import Tuple, Dict


def load_model():

    net = Net(
        train_path="app/Net/image_set/train", 
        test_path="app/Net/image_set/test", 
        valid_path="app/Net/image_set/validator"
        )
    
    # train_generator, test_generator, valid_generator = net.load_image_set()
    model = net.load_model_weights()

    return model


# def execute_model():
#     model, test_generator = load_model()

#     return model.evaluate(test_generator)[1]


def test_post_image(image: str) -> Dict[str, str]:

    """
    :params:image the file of location of the specific 
            image to make the prediction
    """
    # file_path = "temp/image/hola.png"
    model  = load_model()
    
    img = Image.open(image)
    img = img.resize((64,64))
    img = img_to_array(img)
    img = img/255.0
    img = img.reshape(1, 64, 64, 3)

    prediction = model.predict(img)
    prediction[0][0], prediction[0][1], prediction[0][2]
    return {
        "low":f"{prediction[0][0]}",
        "non":f"{prediction[0][1]}",
        "reg":f"{prediction[0][2]}"
    }


def train_model():

    net = Net(
        train_path="app/Net/image_set/train", 
        test_path="app/Net/image_set/test", 
        valid_path="app/Net/image_set/validator"
        )
    
    model = net.run_model()
