CC = clang-3.5

all: main

main: call-function.c
	$(CC) -emit-llvm -S -c call-function.c

clean:
	rm -rvf *.ll
