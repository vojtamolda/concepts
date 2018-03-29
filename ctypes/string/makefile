all: test

clean:
	rm -f *.o *.so

libstring.so: string.c
	clang -shared -Wall -Werror -fpic -o libstring.so string.c

test: libstring.so
	./string.py
