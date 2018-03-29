#!/usr/bin/env bash

./sink.py &
./worker.py &
./worker.py &
./worker.py &
./ventilator.py
