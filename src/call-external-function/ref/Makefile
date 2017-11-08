CC = clang-3.5

all: main

main: call-printf.c
	$(CC) -emit-llvm -S -c call-printf.c

clean:
	rm -rvf *.ll
