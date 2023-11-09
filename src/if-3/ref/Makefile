CC = clang-3.5

all: main

main: if.c
	$(CC) -emit-llvm -S -c if.c

clean:
	rm -rvf *.ll
