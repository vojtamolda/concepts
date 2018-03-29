all: test

clean:
	rm -f *.o *.so

libfunction.so: function.c
	clang -shared -Wall -Werror -fpic -o libfunction.so function.c

test: libfunction.so
	./function.py
