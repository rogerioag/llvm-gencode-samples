CC = clang-3.5

all: main

main:instrucoeslogicas.c
	$(CC) -emit-llvm -S -c instrucoeslogicas.c

clean:
	rm -rvf *.ll
