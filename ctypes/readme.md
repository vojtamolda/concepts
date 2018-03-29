
# Python [`ctypes`](https://docs.python.org/3.6/library/ctypes.html)

_ctypes_ is a foreign function library for Python. It provides C compatible data types, and allows calling functions in
DLLs or shared libraries. It can be used to wrap these libraries in pure Python.



## Call A Function - [`function/`](function/)
- Functions are accessed as attributes of library objects.
- You can call these functions like any other Python callable.

```bash
#!/bin/bash
make test
```


## Allocate Memory for Objects - [`allocate/`](allocate/)
- While basic types, ints and floats, generally get marshalled by _ctypes_ trivially, strings pose a problem. In Python,
  strings are immutable, meaning they cannot change. This produces some odd behavior when passing strings in _ctypes_.
- We need to convert the original string to bytes using `str.encode`, and then pass this to the constructor for a
  `ctypes.string_buffer`. `string_buffer`s are mutable, and they are passed to C as a `char *` as you would expect.
- We need to be aware of which values are being passed as pointers and thus need the `ctypes.POINTER(...)` type applied
  to them. All others are passed by value and can't be modified.

```bash
#!/bin/bash
make test
```


## Interacting Data Structures - [`structure/`](structure/)
- The library consists of two data structures: Point and Line. A Point is a pair of (x, y) coordinates while a Line has
  a start and end point. There are also a handful of functions which modify each of these types.
- The _fields_ attribute of the class `ctypes.Structure` class provides a way to interface with structures. This
  attribute is a list of tuples and allows _ctypes_ to map attributes from Python back to the underlying C structure.

```bash
#!/bin/bash
make test
```
