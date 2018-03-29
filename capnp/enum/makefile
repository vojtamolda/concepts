all: test

clean:
	rm -f *.o enum.run

enum.capnp.h enum.capnp.c++: enum.capnp
	capnp compile enum.capnp -oc++

enum.bin: enum.c++ enum.capnp.c++
	clang++ -std=c++11 -Wall -Werror -lcapnp -lkj -o enum.bin enum.capnp.c++ enum.c++

test: enum.bin enum.py
	./enum.bin
	./enum.py
