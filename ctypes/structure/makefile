all: point line

clean:
	rm -f *.o *.so *.html

libpoint.so: point.o
	clang -shared $^ -o $@

libline.so: point.o line.o
	clang -shared $^ -o $@

%.o: %.c
	clang -c -Wall -Werror -fpic $^

point: libpoint.so
	./point.py

line: libline.so
	./line.py
