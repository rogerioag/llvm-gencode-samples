CC = clang

all: main

main: vars.c
	$(CC) -emit-llvm -S -c vars.c

clean:
	rm -rvf *.ll
