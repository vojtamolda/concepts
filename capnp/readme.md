
# [Cap'n Proto](https://capnproto.org)

_Cap’n Proto_ is an insanely fast data interchange format and capability-based RPC system. Think JSON, except binary.



## Enum Packing - [`enum/`](enum/)
- To generate C++ code from interface definition, use the `capnp` tool - `capnp compile -oc++ enum.capnp`.
- All code needs to be linked with `libcapnp` and `libkj`.

```bash
#!/bin/bash
make test
```
