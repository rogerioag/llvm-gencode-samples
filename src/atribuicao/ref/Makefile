CC = clang

all: main

main: atribuicao.c
	$(CC) -emit-llvm -S -c atribuicao.c

clean:
	rm -rvf *.ll
