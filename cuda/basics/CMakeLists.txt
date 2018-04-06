cmake_minimum_required(VERSION 3.5)
project(cuda_introduction)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS cpp cu)
set(CMAKE_CXX_COMPILER nvcc)


add_executable(add_cpu
        add_cpu.c add_block.cu)

add_executable(add_cuda
        add_cuda.cu)
