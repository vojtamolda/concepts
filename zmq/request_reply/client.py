#!/usr/bin/env python3

# Hello World client in Python
# Connects REQ socket to tcp://localhost:5555
# Sends "Hello" to server, expects "World" back
#

import zmq


context = zmq.Context()
print("Connecting to request_reply world server...")
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for request in range(10):
    print("Sending request {}".format(request))
    socket.send(b"Hello")
    message = socket.recv()
    print("Received reply {} [{}]".format(request, message))
