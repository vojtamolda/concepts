#!/usr/bin/env bash

mkdir build && cd build
cmake ..
make
./add_block
./add_grid
./saxpy
