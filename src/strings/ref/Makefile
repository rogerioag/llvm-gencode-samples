CC = clang

all: main

main: strings.c
	$(CC) -emit-llvm -S -c strings.c

clean:
	rm -rvf *.ll
