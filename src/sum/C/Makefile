CC=clang-3.5

all: compile bc ll obj linking-bc

compile: main.c sum.c
	$(CC) main.c sum.c -o sum-clang.exe

bc: main.c sum.c
	clang-3.5 -emit-llvm -c main.c -o main.bc
	clang-3.5 -emit-llvm -c sum.c -o sum.bc

ll: main.c sum.c
	clang-3.5 -emit-llvm -S -c main.c -o main.ll
	clang-3.5 -emit-llvm -S -c sum.c -o sum.ll

obj: bc
	llc-3.5 -filetype=obj main.bc -o main.o
	llc-3.5 -filetype=obj sum.bc -o sum.o
	clang-3.5 main.o sum.o -o sum-via-obj.exe

linking-bc: bc
	llvm-link-3.5 main.bc sum.bc -o sum-linked.bc
	llc-3.5 -filetype=obj sum-linked.bc -o sum-linked.o
	clang-3.5 sum-linked.o -o sum-via-link-bc-obj.exe

clean:
	rm *.exe *.o *.ll *.bc
