
# [CUDA](https://developer.nvidia.com/cuda-zone)

CUDA is a parallel computing platform and programming model developed by nVidia for general computing on graphical
processing units (GPUs). CUDA allows developers to dramatically speed up computing applications by harnessing the power
of GPUs.


## Basics - [`basics/`](basics/)

- Simple add application for CPU and GPU.

```bash
!#/bin/bash
mkdir build && cd build
cmake ..
make
./add_cpu
./add_cuda
```


## Introduction - [`introduction/`](introduction/)

- Block and grid concepts of GPU parallelization.
- Simple `a*x + y` kernel demo.

```bash
!#/bin/bash
mkdir build && cd build
cmake ..
make
./add_block
./add_grid
./saxpy
```


### Requirements
- [CUDA](https://developer.nvidia.com/cuda-zone/) - nVidia GPU Parallel Programing Framework
