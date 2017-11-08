CC = clang-3.5

all: main

main: array-1d.c
	$(CC) -emit-llvm -S -c array-1d.c

clean:
	rm -rvf *.ll
