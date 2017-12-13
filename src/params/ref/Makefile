CC = clang-3.5

all: main

main: params.c
	$(CC) -emit-llvm -S -c params.c

clean:
	rm -rvf *.ll
