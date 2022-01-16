"""When a POST method it's comming
with a image included in the body,
it's useful try to manage the image and
try to parsing, to send into the 
neural network, make resizing  in the its
pixels, and converting into a tensor, once 
the image parsed it's sent, try to make the
convolution and return the value of the query
with the result"""

import os
from tensorflow.keras.preprocessing.image import (
    ImageDataGenerator,
    load_img,
    img_to_array,
    array_to_image
)
from typing import Any



def process_image(image: Any):
    print(type(image))