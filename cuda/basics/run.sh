#!/usr/bin/env bash

mkdir build && cd build
cmake ..
make
./add_cpu
./add_cuda
