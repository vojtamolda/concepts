#!/usr/bin/env bash

sudo service apache2 start
redis-server
./classifier.py
