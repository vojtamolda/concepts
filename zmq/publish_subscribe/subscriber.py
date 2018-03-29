#!/usr/bin/env python3
#
# Weather Update Client
# Connects SUB socket to tcp://localhost:5556
# Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq


context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect('tcp://localhost:5556')

zip_filter = sys.argv[1] if len(sys.argv) > 1 else '10001'
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

total_temp = 0
for update_nbr in range(5):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

print("Average temperature for zipcode {} was {} F.".format(zip_filter, total_temp / (update_nbr + 1)))
