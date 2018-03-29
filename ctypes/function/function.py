#!/usr/bin/env python3
import ctypes

# Load the library
libfunction = ctypes.CDLL('libfunction.so')

# Call myprint(...) function
libfunction.myprint()

# Call add_one(...) function
a = libfunction.add_one(2)
print("a = {}".format(a))
