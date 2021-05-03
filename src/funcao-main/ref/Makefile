CC = clang

all: main

main: main.c
	$(CC) -emit-llvm -S -c main.c

clean:
	rm -rvf *.ll
