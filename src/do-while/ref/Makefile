CC = clang-3.5

all: main

main: dowhile.c
	$(CC) -emit-llvm -S -c dowhile.c

clean:
	rm -rvf *.ll
