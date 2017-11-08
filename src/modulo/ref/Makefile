CC = clang-3.5

all: main

main: array-2d.c
	$(CC) -emit-llvm -S -c array-2d.c

clean:
	rm -rvf *.ll
