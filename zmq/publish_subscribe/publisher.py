#!/usr/bin/env python3
#
# Weather Update Server
# Binds PUB socket to tcp://*:5556
# Publishes random weather updates
#

import zmq
from random import randrange


context = zmq.Context()
socket = context.socket(zmq.PUB)
print("Starting weather server...")
socket.bind('tcp://*:5556')

while True:
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string("{} {} {}".format(zipcode, temperature, relhumidity))
