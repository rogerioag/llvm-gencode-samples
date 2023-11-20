CC=clang

all: compile bc ll obj linking-bc

compile: main.c sum.c
	$(CC) main.c sum.c -o sum-clang.exe

bc: main.c sum.c
	clang -emit-llvm -c main.c -o main.bc
	clang -emit-llvm -c sum.c -o sum.bc

ll: main.c sum.c
	clang -emit-llvm -S -c main.c -o main.ll
	clang -emit-llvm -S -c sum.c -o sum.ll

obj: bc
	llc -filetype=obj main.bc -o main.o
	llc -filetype=obj sum.bc -o sum.o
	clang main.o sum.o -o sum-via-obj.exe

linking-bc: bc
	llvm-link main.bc sum.bc -o sum-linked.bc
	llc -filetype=obj sum-linked.bc -o sum-linked.o
	clang sum-linked.o -o sum-via-link-bc-obj.exe

clean:
	rm *.exe *.o *.ll *.bc
