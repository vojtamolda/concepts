#!/usr/bin/env python3
import capnp
import enum_capnp


temperature = enum_capnp.Temperature.new_message()
temperature.value = 100
temperature.unit = 'c'

print(temperature)
print(temperature.to_bytes())
