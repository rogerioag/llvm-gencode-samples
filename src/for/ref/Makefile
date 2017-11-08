CC = clang-3.5

all: main

main: for.c
	$(CC) -emit-llvm -S -c for.c

clean:
	rm -rvf *.ll
