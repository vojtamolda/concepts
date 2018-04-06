from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np
import base64


settings = {
    'redis': {
        'host': "localhost",
        'port': 6379,
        'db': 0
    },
    'image': {
        'width': 224,
        'height': 224,
        'channels': 3,
        'dtype': 'float32'
    },
    'queue': {
        'name': 'image-queue',
        'batch_size': 32,
        'server_sleeep': 0.25,
        'classifier_sleep': 0.25
    }
}


def prepare_image(image, target):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    return image


def base64_encode_image(image):
    data = base64.b64encode(image).decode("utf-8")
    return data


def base64_decode_image(data, dtype, shape):
    image = bytes(data, encoding="utf-8")
    image = np.frombuffer(base64.decodestring(image), dtype=dtype)
    image = image.reshape(shape)
    return image
