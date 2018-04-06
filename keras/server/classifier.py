#!/usr/bin/env python3

from keras.applications import ResNet50
from keras.applications import imagenet_utils
import numpy as np
import redis
import time
import json

from utils import settings, prepare_image, base64_decode_image


def queue_classify(database, model):
        queue = database.lrange(settings['queue']['name'], 0, settings['queue']['batch_size'] - 1)
        image_ids, batch = [], None

        for item in queue:
            item = json.loads(item.decode('utf-8'))
            image = base64_decode_image(item['image'], settings['image']['dtype'],
                                        (1, settings['image']['height'], settings['image']['width'], settings['image']['channels']))
            batch = image if batch is None else np.vstack([batch, image])
            image_ids.append(item["id"])

        if len(image_ids) > 0:
            print("* Batch size: {}".format(batch.shape))
            preds = model.predict(batch)
            results = imagenet_utils.decode_predictions(preds)

            for (image_id, result_set) in zip(image_ids, results):
                output = []
                for (imagenet_id, label, prob) in result_set:
                    r = {'label': label, 'probability': float(prob)}
                    output.append(r)
                database.set(image_id, json.dumps(output))
            database.ltrim(settings['queue']['name'], len(image_ids), -1)

        time.sleep(settings['queue']['classifier_sleep'])


if __name__ == '__main__':
    print("* Loading model...")
    database = redis.StrictRedis(**settings['redis'])
    model = ResNet50(weights='imagenet')
    print("* Model loaded")
    while True:
        queue_classify(database, model)
