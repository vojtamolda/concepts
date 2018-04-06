cmake_minimum_required(VERSION 3.5)
project(cuda_introduction)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS cpp cu)
set(CMAKE_CXX_COMPILER nvcc)


add_executable(add_block
        add_block.cu)

add_executable(add_grid
        add_grid.cu)

add_executable(saxpy
        saxpy.cu)
