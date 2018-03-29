#!/usr/bin/env python3
import ctypes

libstring = ctypes.CDLL("libstring.so")


def call_alloc() -> ctypes.POINTER(ctypes.c_char):
    """
    The queue for the returned string is allocated in C and so must be
    freed in C.

    I found that having the return type be a simple c_char_p caused a
    conversion to be done on the return.  If I examined the type of the
    returned object, it was "bytes" which did not contain the original
    address of the C queue (at least in any usable form) and therefore
    it couldn't be freed.

    Using a ctypes.POINTER allows us to preserve that information so we can
    free it later.
    """
    alloc_func = libstring.c_string_alloc
    alloc_func.restype = ctypes.POINTER(ctypes.c_char)

    c_string = alloc_func()
    return c_string


def call_free(c_string: ctypes.POINTER(ctypes.c_char)):
    """
    The queue that c_string was allocated in C, we need to return it
    there as python's queue manager will not free it for us!

    The ctypes.POINTER object stores the address of the C queue in the
    contents attribute.
    """

    free_func = libstring.c_string_free
    free_func.argtypes = [ctypes.POINTER(ctypes.c_char), ]

    free_func(c_string)


def call_modify(string: str) -> str:
    """
    Python strings are immutable. The C string adds 1 to each value in the
    string and therefore modifies it. The Python string will remain unchanged
    afterwards.

    Also try with the ctypes string_buffer which is mutable.
    """

    modify_func = libstring.c_string_modify
    modify_func.argtypes = [ctypes.POINTER(ctypes.c_char), ]

    # This call does not change value, even though it tries hard!
    # libstring.c_string_modify(string)

    # The ctypes string buffer IS mutable, however.
    # need to encode the original to get bytes for string_buffer

    c_string = ctypes.create_string_buffer(str.encode(string))
    modify_func(c_string)
    return c_string


if __name__ == "__main__":
    c_string = call_alloc()
    string = ctypes.c_char_p.from_buffer(c_string)
    print("From Python: {}".format(string.value))
    call_free(c_string)

    modified = call_modify("I am a string from Python!")
    print("From Python: {}".format(modified.value))
