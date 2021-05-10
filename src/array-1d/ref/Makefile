CC = clang

all: main

main: array-1d.c
	$(CC) -emit-llvm -S -c array-1d.c

clean:
	rm -rvf *.ll
