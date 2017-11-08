CC = clang-3.5

all: main

main: while.c
	$(CC) -emit-llvm -S -c while.c

clean:
	rm -rvf *.ll
