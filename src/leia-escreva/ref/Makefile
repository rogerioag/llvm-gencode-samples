CC = clang-3.5

all: main

main: main-c.c
	$(CC) -emit-llvm -S -c main-c.c
	$(CC) -emit-llvm -S -c io.c

clean:
	rm -rvf *.ll
