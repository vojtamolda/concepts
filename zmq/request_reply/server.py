#!/usr/bin/env python3

# Hello World server in Python
# Binds REP socket to tcp://*:5555
# Expects b"Hello" from client, replies with b"World"
#

import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
print("Starting request_reply world server...")
socket.bind('tcp://*:5555')

while True:
    message = socket.recv()
    print("Received request: {}".format(message))
    time.sleep(1)
    socket.send(b"World")
