import time
import requests
import threading
import unittest


class TestClassificationServer(unittest.TestCase):
    RequestCount = 500
    SleepDuration = 0.05
    ImageFilename = './image.png'
    URL = 'http://localhost:5000/predict'

    def test_request(self):
        request = self.classification_request()
        self.assertTrue(request["success"])
        for (i, result) in enumerate(request["predictions"]):
            print("{}. {}: {:.4f}".format(i + 1, result["label"], result["probability"]))

    def test_high_load(self):
        for _ in range(self.RequestCount):
            worker = threading.Thread(target=self.classification_request, args=(self, ))
            worker.daemon = True
            worker.start()
            time.sleep(self.SleepDuration)
        # Wait until server is done with processing
        time.sleep(300)

    @classmethod
    def classification_request(cls):
        image = open(cls.ImageFilename, "rb").read()
        request = requests.post(cls.URL, files={"image": image}).json()
        return request
