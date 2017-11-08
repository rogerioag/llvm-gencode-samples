CC = clang-3.5

all: main

main: funcao.c
	$(CC) -emit-llvm -S -c funcao.c

clean:
	rm -rvf *.ll
