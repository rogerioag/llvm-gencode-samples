CC = clang-3.5

all: main

main: coercao.c
	$(CC) -emit-llvm -S -c coercao.c

clean:
	rm -rvf *.ll
