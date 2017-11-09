CC = clang-3.5

all: main

main: vars.c
	$(CC) -emit-llvm -S -c vars.c

clean:
	rm -rvf *.ll
