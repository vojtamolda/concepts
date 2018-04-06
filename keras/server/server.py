#!/usr/bin/env python3

from PIL import Image
import redis
import flask
import uuid
import time
import json
import io

from utils import settings, prepare_image, base64_encode_image


server = flask.Flask("Keras Scalable REST Model Server")
database = redis.StrictRedis(**settings['redis'])


@server.route("/")
def homepage() -> str:
    return "Welcome to Keras Scalable REST Model Server!"


@server.route("/predict", methods=['POST'])
def predict() -> str:
    data = {'success': False}

    if flask.request.method == 'POST':
        if flask.request.files.get('image'):
            # Prepare image for processing
            image = flask.request.files['image'].read()
            image = Image.open(io.BytesIO(image))
            image = prepare_image(image, (settings['image']['width'], settings['image']['height']))
            image = image.copy(order='C')

            # Push the image to the queue
            k = str(uuid.uuid4())
            image = base64_encode_image(image)
            d = {'id': k, 'image': image}
            database.rpush(settings.queue['name'], json.dumps(d))

            # Poll the queue for results
            while True:
                output = database.get(k)
                if output is None:
                    time.sleep(settings.queue['server_sleep'])
                    continue
                output = output.decode('utf-8')
                data['predictions'] = json.loads(output)
                database.delete(k)
                break
            data['success'] = True

    return flask.jsonify(data)


if __name__ == '__main__':
    server.run()
