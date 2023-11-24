CC = clang

all: main link compile

main: nested-call-function.c io.c
	$(CC) -fno-discard-value-names -c -S -emit-llvm nested-call-function.c
	$(CC) -fno-discard-value-names -c -S -emit-llvm io.c

link: io.ll nested-call-function.ll
	llvm-link -S nested-call-function.ll io.ll -o nested-call-function-linked.ll

compile: nested-call-function-linked.ll
	$(CC) nested-call-function-linked.ll -o nested-call-function-linked.exe

clean:
	rm -rvf *.ll *.exe

